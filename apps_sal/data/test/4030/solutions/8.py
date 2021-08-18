
import sys


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


INF = 10 ** 18
MOD = 10 ** 9 + 7


def bisearch_min(mn, mx, func):
    ok = mx
    ng = mn
    while ng + 1 < ok:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok


def check(m):
    if m == len(B):
        return True
    if B[m][-1][0] <= a:
        return True
    else:
        return False


N = INT()
A = [ord(c) - 97 for c in input()]

B = [[] for i in range(1)]
B[0].append((A[0], 0))
for i, a in enumerate(A[1:], 1):
    idx = bisearch_min(-1, len(B), check)
    if idx == len(B):
        B.append([(a, i)])
    else:
        B[idx].append((a, i))

ans = [0] * N
for a, li in enumerate(B):
    for _, idx in li:
        ans[idx] = a + 1
print(len(B))
print(*ans)
