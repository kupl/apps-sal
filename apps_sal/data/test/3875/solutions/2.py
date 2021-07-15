SIZE=10; MOD=10**9+7 #998244353 #ここを変更する
inv = [0]*SIZE
inv[1] = 1
for i in range(2,SIZE):
    inv[i] = MOD - (MOD//i)*inv[MOD%i]%MOD

def solve(a):
    n = len(a)
    for i in range(n-2,-1,-1):
        if a[i] > a[i+1]: a[i] = a[i+1]
    if a[0] < 0: return 0
    A = a[-1]+1
    res = [[0,0,1]]
    for ai in a:
        val = 0
        for r in res:
            bi,ki,ti = r
            val += ti
            r[1] += 1
            r[2] = r[2]*(A-bi+ki+1)%MOD*inv[ki+1]%MOD
        res.append([ai+1,1,-val%MOD*(A-ai)%MOD])
    return sum(r[2] for r in res)%MOD

from bisect import bisect_left
def LIS(a):
    n = len(a)
    dp = [n+1]*n
    for i in a:
        dp[bisect_left(dp,i)] = i
    return bisect_left(dp,n+1)

from itertools import permutations
n = int(input())
*a, = map(int, input().split())
ans = 0
for x in permutations(range(n)):
    b = [a[i]-1 for i in x]
    offset = 0
    for i in range(n):
        b[i] -= offset
        if i+1<n and x[i] < x[i+1]:
            offset += 1
    ans += LIS(x)*solve(b)
    ans %= MOD

c = 1
for i in a:
    c *= i
    c %= MOD
ans *= pow(c,MOD-2,MOD)
print(ans%MOD)
