n,m=list(map(int,input().split()))
low=1000000000000000000000000
for i in range(n):
    a,b=list(map(int,input().split()))
    if (a/b)*m < low:
        low = (a/b)*m
print(low)

