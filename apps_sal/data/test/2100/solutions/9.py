n=int(input())

x,y=0,0
for i in range(n):
    a,b=list(map(int,input().split()))
    x+=a
    y+=b
print(min(x,n-x)+min(y,n-y))



