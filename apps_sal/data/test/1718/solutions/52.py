n,k = map(int,input().split())
n -= k
if n%(k-1) == 0:
    print(1+n//(k-1))
else:
    print(2+n//(k-1))
