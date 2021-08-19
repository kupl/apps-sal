(n, m, k, x, y) = list(map(int, input().split()))
x -= 1
y -= 1
if n == 1:
    print((k + m - 1) // m, k // m, k // m + (k % m > y))
else:
    cnt = m * (n + n - 2)
    k -= 1
    c = [[k // cnt * (1 + (0 < i < n - 1)) + (k % cnt >= i * m + j) + (0 < i < n - 1) * (k % cnt >= n * m + (n - i - 2) * m + j) for j in range(m)] for i in range(n)]
    print(max([max(c[i]) for i in range(n)]), min([min(c[i]) for i in range(n)]), c[x][y])
