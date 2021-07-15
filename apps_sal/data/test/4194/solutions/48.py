n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

if n >= sum(a):
    print((n-sum(a)))
else:
    print((-1))

