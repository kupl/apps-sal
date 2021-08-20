def main():
    (n, m, k, x, y) = list(map(int, input().split()))
    A = [[0] * m for i in range(n)]
    MOD = (2 * n - 2) * m
    if n > 1:
        for i in range(m):
            A[0][i] += k // MOD
            A[-1][i] += k // MOD
        for i in range(1, n - 1):
            for j in range(m):
                A[i][j] += 2 * (k // MOD)
        k %= MOD
        for i in range(n):
            for j in range(m):
                if k > 0:
                    A[i][j] += 1
                    k -= 1
        for i in range(n - 2, -1, -1):
            for j in range(m):
                if k > 0:
                    A[i][j] += 1
                    k -= 1
    else:
        MOD = m
        for i in range(m):
            A[0][i] = k // MOD
        k %= MOD
        for i in range(m):
            if k > 0:
                A[0][i] += 1
                k -= 1
    maxx = -1
    minn = 10 ** 100
    for row in A:
        maxx = max(maxx, max(row))
        minn = min(minn, min(row))
    print(maxx, minn, A[x - 1][y - 1])


main()
