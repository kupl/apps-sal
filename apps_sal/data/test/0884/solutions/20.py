"""http://codeforces.com/problemset/problem/869/C"""

def calc(x,y):
    si, ans = 1, 1
    n,m = min(x,y), max(x,y)
    for i in range(1,n+1):
        si = (si * (n-i+1) * (m-i+1) // i)
        ans = (ans + si)
    return ans % MOD


MOD = 998244353
a,b,c = list(map(int, input().split()))
rb = calc(a,b)
rp = calc(a,c)
bp = calc(b,c)
res = rb*rp*bp % MOD
print(res)


