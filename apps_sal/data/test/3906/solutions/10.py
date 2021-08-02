n, m = map(int, input().split())
d = [2, 4]
k = 10**9 + 7
for i in range(2, max(n, m)):
    d += [(d[i - 1] + d[i - 2]) % k]
print((d[m - 1] + d[n - 1] - 2) % k)
