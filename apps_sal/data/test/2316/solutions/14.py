t=int(input())
for _ in range(t):
    x,n,m=list(map(int,input().split()))
    for i in range(n):
        a=x//2+10
        if a>=x:
            break
        else:
            x=a
    for i in range(m):
        x=x-10
    if x<=0:
        print("YES")
    else:
        print("NO")
