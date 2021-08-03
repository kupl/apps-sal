n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == 0:
        ans += t
    elif a[i - 1] + t <= a[i]:
        ans += t
    else:
        ans += a[i] - a[i - 1]
print(ans)
