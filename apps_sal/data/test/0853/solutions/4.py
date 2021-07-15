n=int(input())

A=list(map(int,input().split()))

A.sort()

if(A.count(0)==0):
    print(-1)
else:
    ans="0"*A.count(0)
    x=A.count(5)
    while((x*5)%9!=0):
        x-=1
    ans=("5"*x)+ans
    if( "5" not in ans ):
        print(0)
    else:
        print(ans)

