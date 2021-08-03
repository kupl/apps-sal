n = int(input())
h = [0] + list(map(int, input().split())) + [0]
ma = 0
mi = float('inf')
ans = 0
for i in range(n + 1):
    if h[i] <= h[i + 1]:
        ma = max(ma, h[i + 1])
        mi = min(mi, h[i])
    else:
        ans += ma - mi
        ma = h[i + 1]
        mi = h[i + 1]
print(ans)
