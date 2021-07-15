n,m = list(map(int,input().split()))
n, m = min(n,m),max(n,m)

if n == 1 and m == 1:
    print((1))
elif n == 1:
    print((m-2))
elif n == 2:
    print((0))
else:
    print(((n*m)-(2*n)-(2*m)+4))

