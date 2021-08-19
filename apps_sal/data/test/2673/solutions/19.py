"""
-----------------------------Pseudo---------------------------------
"""
import copy
import sys
from collections import defaultdict, Counter


def input():
    return sys.stdin.readline()


def mapi():
    return map(int, input().split())


def maps():
    return map(str, input().split())


def print(arg, *argv, end=None):
    sys.stdout.write(str(arg))
    for i in argv:
        sys.stdout.write(' ' + str(i))
    sys.stdout.write(end) if end else sys.stdout.write('\n')


def solve():
    t = 1
    while t:
        t -= 1
        a = input().strip()
        n = len(a)
        g = defaultdict(list)
        for i in range(n):
            g[a[i]].append(i)
        vis = {}
        vis[0] = 0
        q = [0]
        while len(q) != 0:
            tmp = q.pop(0)
            if tmp == n - 1:
                break
            val = a[tmp]
            x = len(g[val])
            for i in range(x):
                if g[val][i] not in vis:
                    q.append(g[val][i])
                    vis[g[val][i]] = vis[tmp] + 1
            g[val] = []
            if tmp + 1 <= n - 1 and tmp + 1 not in vis:
                q.append(tmp + 1)
                vis[tmp + 1] = vis[tmp] + 1
            if tmp - 1 >= 0 and tmp - 1 not in vis:
                q.append(tmp - 1)
                vis[tmp - 1] = vis[tmp] + 1
        print(vis[n - 1])


def __starting_point():
    solve()


__starting_point()
