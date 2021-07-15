# n=int(input())
n,k=(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
mid=n//2
for i in range(mid,n-1):
    if k-(a[i+1]-a[i])*(i-mid+1)>=0:
        k-=(a[i+1]-a[i])*(i-mid+1)
    else:
        print(k//(i-mid + 1) + a[i]);return
print(k//(n-mid) + a[-1])

        
