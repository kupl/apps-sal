n=int(input())
a=list(map(int,input().split()))
a.sort()
coins=0
for i in range(n):
    if i-1>=0 and a[i]<=a[i-1]:
        coins+=a[i-1]-a[i]+1
        a[i]=a[i-1]+1
print(coins)

