n,m,k = map(int,input().split())
if n >= k:
    print(n-k,m)
else:
    if m - (k-n) < 0:
        m = 0
    else:
        m -= k - n
    print(0,m)
