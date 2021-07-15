import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c for j in range(b)] for i in range(a)]
def list3d(a, b, c, d): return [[[d for k in range(c)] for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e for l in range(d)] for k in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10**19
MOD = 10**9 + 7
EPS = 10**-10

N = INT()
S = input()

dp0 = [0] * (N+1)
dp1 = [0] * (N+1)
dp2 = [0] * (N+1)
dp3 = [0] * (N+1)
dp0[0] = 1
for i in range(N):
    if S[i] == 'a':
        dp0[i+1] += dp0[i]
        dp1[i+1] += dp1[i]
        dp2[i+1] += dp2[i]
        dp3[i+1] += dp3[i]
        dp1[i+1] += dp0[i]
    elif S[i] == 'b':
        dp0[i+1] += dp0[i]
        dp1[i+1] += dp1[i]
        dp2[i+1] += dp2[i]
        dp3[i+1] += dp3[i]
        dp2[i+1] += dp1[i]
    elif S[i] == 'c':
        dp0[i+1] += dp0[i]
        dp1[i+1] += dp1[i]
        dp2[i+1] += dp2[i]
        dp3[i+1] += dp3[i]
        dp3[i+1] += dp2[i]
    else:
        dp0[i+1] += dp0[i]*3
        dp1[i+1] += dp1[i]*3
        dp2[i+1] += dp2[i]*3
        dp3[i+1] += dp3[i]*3
        dp1[i+1] += dp0[i]
        dp2[i+1] += dp1[i]
        dp3[i+1] += dp2[i]
    dp0[i+1] %= MOD
    dp1[i+1] %= MOD
    dp2[i+1] %= MOD
    dp3[i+1] %= MOD
ans = dp3[N]
print(ans)

