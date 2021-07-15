import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for k in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10**9)
INF = 10**19
MOD = 10**9 + 7
EPS = 10**-10

N = INT()
T = input()

K = 10**10
mod = 3
S = '110'

if T == '1':
    print((K*2))
    return
if T == '11' or T == '10' or T == '0':
    print(K)
    return

def check(m):
    for i in range(N):
        if T[i] != S[(i+m)%mod]:
            return False
    return True

for m in range(mod):
    if check(m):
        N -= 3-m
        ans = K - ceil(N, 3)
        print(ans)
        break
else:
    print((0))

