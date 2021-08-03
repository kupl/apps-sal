a = list(map(int, input().split()))
ans = 0
if a[0] > a[1]:
    ans += a[0]
    a[0] -= 1
else:
    ans += a[1]
    a[1] -= 1
if a[0] > a[1]:
    ans += a[0]
else:
    ans += a[1]
print(ans)
