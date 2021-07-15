n,k=map(int,input().split())
ori=k
if n==1 or k<=2:
    print(0)
    return
if k%2==0: k-=1
first=k//2
second=ori-first
if second>n:
    print(0)
    return
print(min(first,n-second+1))
