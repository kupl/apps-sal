import sys

# import bisect
# from collections import deque
# sys.setrecursionlimit(100000)


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
MOD = 10 ** 9 + 7

n = int(ri())
lis = [[] for i in range(n)]
for _ in range(n - 1):
    a, b = Ri()
    a -= 1
    b -= 1
    lis[a].append(b)
    lis[b].append(a)
visit = [-1] * n
no = [1] * n
sta = [0]
visit[0] = True
if n & 1 == 1:
    print(-1)
else:
    while len(sta) > 0:
        top = sta[-1]
        ret = True
        for i in range(len(lis[top])):
            if visit[lis[top][i]] == -1:
                visit[lis[top][i]] = top
                ret = False
                sta.append(lis[top][i])
        if ret:
            if top != 0:
                no[visit[top]] += no[top]
            sta.pop()
    ans = 0
    no = no[1:]
    for i in no:
        if i & 1 == 0:
            ans += 1
    print(ans)
