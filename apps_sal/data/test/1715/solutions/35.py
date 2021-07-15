def main():
    from bisect import bisect_left
    A, B, Q = list(map(int, input().split()))
    INF = 2 * 10 ** 10
    S = [-INF] + [int(input()) for _ in range(A)] + [INF]
    T = [-INF] + [int(input()) for _ in range(B)] + [INF]
    S_rev = [-s for s in S][::-1]
    T_rev = [-t for t in T][::-1]

    for q in range(Q):
        x = int(input())
        ans = 5 * 10 ** 10

        # Case1: 右に直進
        cost1_s = S[bisect_left(S, x)] - x
        cost1_t = T[bisect_left(T, x)] - x
        ans = min(ans, max(cost1_s, cost1_t))

        # Case2: 左に直進
        cost2_s = S_rev[bisect_left(S_rev, -x)] + x
        cost2_t = T_rev[bisect_left(T_rev, -x)] + x
        ans = min(ans, max(cost2_s, cost2_t))

        # Case3: 右でS、左でT
        cost3_s = S[bisect_left(S, x)] - x
        cost3_t = T_rev[bisect_left(T_rev, -x)] + x
        ans = min(ans, 2 * min(cost3_s, cost3_t) + max(cost3_s, cost3_t))

        # Case4: 右でT、左でS
        cost3_s = S_rev[bisect_left(S_rev, -x)] + x
        cost3_t = T[bisect_left(T, x)] - x
        ans = min(ans, 2 * min(cost3_s, cost3_t) + max(cost3_s, cost3_t))

        print(ans)


def __starting_point():
    main()

__starting_point()
