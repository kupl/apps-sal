n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    num = a[i]+a[i+1]-x
    if num > 0:
        a[i+1] = max(a[i+1]-num, 0)
        ans += num
print(ans)

