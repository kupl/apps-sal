n, k = map(int, input().split())
h = []
for i in range(n):
    h.append(int(input()))
h.sort()
ans = h[k - 1] - h[0]
for i in range(1, n - k + 1):
    ans = min(ans, h[i + k - 1] - h[i])
print(ans)
