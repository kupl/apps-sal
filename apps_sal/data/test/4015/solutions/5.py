N,M=list(map(int,input().split()))
d = M/N
if not d.is_integer():
    print(-1)
else:
    d = int(d)
    n = 0
    while d and d%2==0:
        n += 1
        d >>= 1
    while d and d%3==0:
        n += 1
        d //= 3
    if d == 1:
        print(n)
    else:
        print(-1)

