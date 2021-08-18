import sys
from math import log2, floor, ceil, sqrt


def Ri(): return [int(x) for x in sys.stdin.readline().split()]
def ri(): return sys.stdin.readline().strip()


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
MOD = 10**9 + 7

a = int(ri())
st = ri()
arr = [int(i) for i in st]
dic = {}
cnt = 0
nz = 0
for i in range(len(st)):
    summ = 0
    for j in range(i, len(st)):
        summ += arr[j]
        if summ != 0:
            nz += 1
        if summ in dic:
            dic[summ] += 1
        else:
            dic[summ] = 1
if a != 0:
    for i in dic:
        if i != 0:
            val = a / i
            if val in dic:
                cnt = cnt + dic[val] * dic[i]
    print(cnt)
else:
    n = len(st)
    print(n**2 * (n + 1)**2 // 4 - nz * nz)
