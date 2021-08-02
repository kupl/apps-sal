import sys

n, m, k = list(map(int, sys.stdin.readline().strip().split()))
a = list(map(int, sys.stdin.readline().strip().split()))
b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = b[i - 1] + m * a[i - 1] - k
M = [10 ** 20] * m
ans = 0
for i in range(0, n + 1):
    M[i % m] = min([M[i % m], b[i]])
    for j in range(0, m):
        if i > j:
            ans = max([ans, b[i] - M[j] - k * ((m * i + m - (i - j)) % m)])
    # print(j, M, ans)
print(ans // m)
