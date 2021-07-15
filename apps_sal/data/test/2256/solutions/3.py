t=int(input())
for _ in range(t):
    n,x,a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    print(min(x+abs(a-b),n-1))
