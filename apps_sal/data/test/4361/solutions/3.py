n, k = map(int, input().split())
h = []
for i in range(n):
    h_ = int(input())
    h.append(h_)
h.sort()
ans = float('inf')
for i in range(n - k + 1):
    ans = min(ans, h[i + k - 1] - h[i])
print(ans)
