n = int(input())
h = list(map(int, input().split()))
ans = 0
maxh = 0
for i in range(n):
    if h[i] >= maxh:
        ans += 1
        maxh = h[i]
print(ans)
