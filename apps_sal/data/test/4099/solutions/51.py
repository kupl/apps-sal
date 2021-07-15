n,k,m = map(int,input().split())
a = list(map(int,input().split()))

if m > (sum(a) + k) / (len(a) + 1):
    print(-1)
elif m < (sum(a)) / (len(a) + 1):
    print(0)
else:
    print((m * (len(a) + 1)) - sum(a) )
