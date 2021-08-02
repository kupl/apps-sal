n, k = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
b = sorted(l)
ans = b[k - 1] - b[0]
for i in range(n - k + 1):
    ans = min(ans, b[i + k - 1] - b[i])
print(ans)
