
from sys import stdin
import sys
sys.setrecursionlimit(300000)


def dfs(v, pa):

    good = 0
    bad = 0
    for nex in lis[v]:
        if nex != pa:
            nans, ng, nb = dfs(nex, v)
            if not nans:
                return nans, 0, 0
            good += ng
            bad += nb

    num = good + bad + p[v]
    if (num - h[v]) % 2 == 0:
        newbad = (num - h[v]) // 2
    else:
        return False, 0, 0
    newgood = num - newbad

    if newbad - p[v] > bad or newgood < good or newbad < 0 or newgood < 0:
        return False, 0, 0
    else:
        return True, newgood, newbad


tt = int(stdin.readline())

for loop in range(tt):

    n, m = list(map(int, stdin.readline().split()))
    p = list(map(int, stdin.readline().split()))
    h = list(map(int, stdin.readline().split()))

    lis = [[] for i in range(n)]
    for i in range(n - 1):
        v, u = list(map(int, stdin.readline().split()))
        v -= 1
        u -= 1
        lis[v].append(u)
        lis[u].append(v)

    ans, good, bad = dfs(0, 0)

    if ans:
        print("YES")
    else:
        print("NO")
