n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    t -= (86400 - a[i])
    if t <= 0:
        ans = i + 1
        break

print(ans)
