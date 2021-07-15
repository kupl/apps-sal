n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
id = n//2
for i in range(n//2,n-1):
    if (a[i+1]-a[i])*(i+1-id)>k:
        print(a[i]+k//(i+1-id))
        return
    else:
        k-=(a[i+1]-a[i])*(i+1-id)
print(a[-1]+k//(n-id))
