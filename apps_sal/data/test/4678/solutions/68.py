n = int(input())
a = list(map(int,input().split()))
ans = 0
if a == sorted(a):
    print(ans)
    return
for i in range(n-1):
    if a[i] > a[i+1]:
        ans = ans + a[i]-a[i+1]
        a[i+1] = a[i]        
print(ans)
