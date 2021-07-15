n,k=map(int,input().split())
a=n%k
if abs(a-k)<=a:
    print(abs(a-k))
else:
    print(a)
