def main():
    import sys
    input = sys.stdin.readline
    (H, W, D) = [int(x) for x in input().strip().split()]
    M = [0] * H
    C = {}
    revM = {}
    for h in range(H):
        M[h] = [int(x) for x in input().strip().split()]
        for (i, w) in enumerate(M[h]):
            revM[w] = (h, i)
    Q = int(input())
    HW = H * W
    ans = [0] * (HW + 1)
    for i in range(1, D + 1):
        cur = i
        while cur + D <= HW:
            ans[cur + D] += ans[cur] + abs(revM[cur][0] - revM[cur + D][0]) + abs(revM[cur][1] - revM[cur + D][1])
            cur += D
    for q in range(Q):
        (l, r) = [int(x) for x in input().strip().split()]
        print(ans[r] - ans[l])


def __starting_point():
    main()


__starting_point()
