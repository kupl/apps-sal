n=int(input())
T=0; X=0; Y=0;
ans="Yes"
for i in range(n):
    t,x,y=map(int,input().split())
    s=t-T
    if s >= abs(X-x)+abs(Y-y) and (s-abs(X-x)+abs(Y-y))%2==0:
        T,X,Y = t,x,y
    else:
        ans="No"
        break
print(ans)
