def solve():
    (n, k) = map(int, input().split())
    c = [[-1 for i in range(n + 1)] for i in range(k)]
    dp = [0 for i in range(n + 1)]
    a = []
    for i in range(k):
        b = list(map(int, input().split()))
        for (j, v) in enumerate(b):
            c[i][v] = j
        a.append(b)
    for i in range(n):
        curpos = a[0][i]
        dp[i] = 1
        for j in range(i):
            prevpos = a[0][j]
            ok = True
            for p in range(k):
                if c[p][curpos] < c[p][prevpos]:
                    ok = False
                    break
            if ok:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
    return


def main():
    t = 1
    for _ in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
