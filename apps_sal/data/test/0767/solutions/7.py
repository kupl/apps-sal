def solve():
    (N, Z) = map(int, input().split())
    X = [int(k) for k in input().split()]
    X.sort()
    ans = 0
    i = 0
    mid = N // 2 + (1 if N % 2 else 0)
    j = mid
    while i < mid and j < N:
        while j < N and X[j] - X[i] < Z:
            j += 1
        if j != N:
            ans += 1
        i += 1
        j += 1
    print(ans)


def __starting_point():
    solve()


__starting_point()
