n,m = map(int,input().split())
if (n,m) == (1,1):
    print(1)
elif n == 1 or m == 1:
    print(max(1,n-2)*max(1,m-2))
else:
    print((n-2)*(m-2))
