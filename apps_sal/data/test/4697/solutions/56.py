n,m = map(int,input().split())
if 2*n >= m:
    print(m // 2)
else:
    print(n+((m-2*n) // 4))
