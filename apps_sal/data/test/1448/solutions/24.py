n,d=list(map(int,input().split()))
m=int(input())
for i in range(m):
    x,y=list(map(int,input().split()))
    if(x<0 or y<0 or x>n or y>n or x+y<d or y+n-x<n-d or n-y+x<n-d or n+n-x-y<d):
        print("NO")
    else:
        print("YES")

