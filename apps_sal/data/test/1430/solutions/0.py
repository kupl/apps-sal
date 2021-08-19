def solve(N, K, S):
    S = [int(s) for s in S]
    point_l = 0
    point_r = 0
    num_0 = 0 if S[0] == 1 else 1
    flg = S[0]
    for i in range(N):
        if S[i] != flg:
            if flg == 1:
                num_0 += 1
                if num_0 > K:
                    point_r = i - 1
                    break
            flg = S[i]
        if i == N - 1:
            point_r = i
            break
    ans = point_r - point_l + 1
    while point_r < N - 1:
        for i in range(0, N):
            if S[point_l + i] != S[point_l + i + 1]:
                if S[point_l + i + 1] == 1:
                    point_l += i + 1
                    break
        for i in range(1, N):
            if point_r + i == N - 1:
                point_r = N - 1
                break
            if S[point_r + i] != S[point_r + i + 1]:
                if S[point_r + i + 1] == 0:
                    point_r += i
                    break
        ans = max(ans, point_r - point_l + 1)
    print(ans)


def __starting_point():
    (N, K) = list(map(int, input().split()))
    S = input()
    solve(N, K, S)


__starting_point()
