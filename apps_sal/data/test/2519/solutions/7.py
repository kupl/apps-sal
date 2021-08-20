(n, k) = map(int, input().split())
p = list(map(int, input().split()))
data = [0] * n
for i in range(n):
    data[i] = p[i] / 2 + float(0.5)
res = sum(data[0:k])
ans = sum(data[0:k])
for i in range(n - k):
    res -= data[i] - data[i + k]
    ans = max(ans, res)
print(ans)
