n, m = map(int, input().split())
a, M, d = 1, 10**9 + 7, [1]
for i in range(n):
    d.append(((m - n + i) * d[i] + i * d[i - 1]) % M)
    a = a * (m - i) % M
print(a * d[-1] % M)
