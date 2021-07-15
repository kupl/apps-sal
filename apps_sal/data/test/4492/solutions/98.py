n,x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
if a[0] > x:
    b = a[0] - x
    ans = b
    a[0] -= b
for i in range(1,n):
    if a[i-1] + a[i] > x:
        b = a[i-1] + a[i] - x
        ans += b
        a[i] -= b
print(ans)
