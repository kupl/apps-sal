(n, k) = map(int, input().split())
h = []
for i in range(n):
    h.append(int(input()))
h.sort()
ans = 1000000000
for j in range(n - k + 1):
    s = h[j + k - 1] - h[j]
    if s < ans:
        ans = s
print(ans)
