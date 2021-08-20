import os
from io import BytesIO
import sys
import threading
sys.setrecursionlimit(10 ** 9)
threading.stack_size(67108864)


def main():

    def ad(i, j):
        nonlocal g
        if j in g[i]:
            g[i].remove(j)
            g[j].remove(i)
        else:
            g[i].add(j)
            g[j].add(i)

    def dfs(v):
        nonlocal used, g, nans
        used[v] = True
        nans.append(v + 1)
        for el in g[v]:
            if not used[el]:
                dfs(el)
    for _ in range(int(input())):
        n = int(input())
        cnt = [set() for i in range(n)]
        g = [set() for i in range(n)]
        used = [False] * n
        triangles = []
        for i in range(n - 2):
            (a, b, c) = map(int, input().split())
            a -= 1
            b -= 1
            c -= 1
            cnt[a].add(i)
            cnt[b].add(i)
            cnt[c].add(i)
            triangles.append((a, b, c))
            ad(a, b)
            ad(b, c)
            ad(a, c)
        q = []
        ones = []
        for i in range(n):
            if len(cnt[i]) == 1:
                ones.append(i)
        ans = []
        nans = []
        for i in range(n - 2):
            t = ones.pop()
            ind = cnt[t].pop()
            ans.append(ind + 1)
            cnt[triangles[ind][0]].discard(ind)
            cnt[triangles[ind][1]].discard(ind)
            cnt[triangles[ind][2]].discard(ind)
            if len(cnt[triangles[ind][0]]) == 1:
                ones.append(triangles[ind][0])
            if len(cnt[triangles[ind][1]]) == 1:
                ones.append(triangles[ind][1])
            if len(cnt[triangles[ind][2]]) == 1:
                ones.append(triangles[ind][2])
        dfs(0)
        print(*nans)
        print(*ans)


tt = threading.Thread(target=main)
tt.start()
