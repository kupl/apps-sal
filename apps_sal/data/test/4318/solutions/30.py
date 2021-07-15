n = int(input())
h = list(map(int, input().split()))
ans = 0
a = 0
for i in range(n):
    if a <= h[i]:
        ans += 1
    if a < h[i]:
        a = h[i]
print(ans)
