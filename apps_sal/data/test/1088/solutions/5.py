def main():
    import sys
    from collections import Counter
    from math import factorial
    input = sys.stdin.readline
    MOD = 998244353
    N, K = [int(x) for x in input().strip().split()]
    A = [0 for n in range(N)]
    for n in range(N):
        A[n] = [int(x) for x in input().strip().split()]
    ans = 1

    def find(x):
        if c[x] == x:
            return x
        c[x] = find(c[x])
        return c[x]
    c = [n for n in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            for n in range(N):
                if A[n][i] + A[n][j] > K:
                    break
            else:
                if c[j] > c[i]:
                    c[j] = c[i]
                else:
                    c[i] = c[j]
    for i in range(N):
        find(i)
    for d in Counter(c).values():
        ans = (ans * factorial(d)) % MOD
    c = [n for n in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            for n in range(N):
                if A[i][n] + A[j][n] > K:
                    break
            else:
                if c[j] > c[i]:
                    c[j] = c[i]
                else:
                    c[i] = c[j]
    for i in range(N):
        find(i)
    for d in Counter(c).values():
        ans = (ans * factorial(d)) % MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
