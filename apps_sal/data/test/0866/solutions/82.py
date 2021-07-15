def getComb(n, k, MOD):
    if n < k:
        return 0
    if n-k < k:
        k = n-k
    comb = 1
    for x in range(n-k+1, n+1):
        comb = (comb*x)%MOD
    d = 1
    for x in range(1, k+1):
        d = (d*x)%MOD
    comb *= pow(d, MOD-2, MOD)
    return comb%MOD


x, y = map(int, input().split())

if (x+y)%3 == 0:
    n = (x+y)//3
    if x < n or y < n:
        ans = 0
    else:
        MOD = 10**9+7
        ans = getComb(n, x-n, MOD)
else:
    ans = 0
    
print(ans)
