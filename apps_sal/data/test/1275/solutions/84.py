N, K = map(int, input().split())
K = abs(K)
num = [0] * (2 * N + 1)
for v in range(2, 2 * N + 1):
    num[v] = min(v - 1, 2 * N + 1 - v)
res = 0
for v in range(K, 2 * N + 1):
    res += num[v] * num[v - K]
print(res)
