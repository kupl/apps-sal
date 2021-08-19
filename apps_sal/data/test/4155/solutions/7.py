n = int(input())
h = list(map(int, input().split()))
hmax = max(h)
ans = 0
f = False
for i in range(1, hmax + 1):
    for j in range(n):
        if f and h[j] < i:
            ans += 1
        f = h[j] >= i
    if f:
        ans += 1
    f = False
print(ans)
