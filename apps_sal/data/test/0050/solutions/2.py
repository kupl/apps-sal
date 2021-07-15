n,m,r = map(int,input().split())
buy = min(map(int,input().split()))
sell = max(map(int,input().split()))

if buy < sell:
    units = r//buy
    print (units*sell + r - (units*buy))
else:
    print (r)
