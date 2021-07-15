n,k = map(int,input().split())
a = abs(n-k*(n//k))
b = abs(n-k*(-(-n//k)))
print(min(a,b))
