n,d=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
for i in range(1,n+1):
    for j in range(i):
        if a[n-i+j]-a[j]<=d:
            print(i-1)
            return

