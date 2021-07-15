x,y = map(int, input().split())
n = int(input())
INF = 10**9+7
if n == 1:
    print(x%INF)
elif n == 2:
    print(y%INF)
else:
    n=n%6
    a=[x,y,y-x,-x,-y,x-y]
    print(a[n-1]%INF)
