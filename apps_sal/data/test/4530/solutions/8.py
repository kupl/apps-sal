t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    ls=[0 for i in range(n+1)]
    for i in range(n):
        ls[a[i]]+=1
    dis=len(set(a))
    sam=max(ls)
    print(max(min(dis-1,sam),min(dis,sam-1)))
    t-=1    
