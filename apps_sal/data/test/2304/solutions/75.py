import sys
from typing import List, Optional

sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))

g = [[] for _ in range(N)]

for i in range(M):
    l, r, d = list(map(int, input().split()))
    l -= 1
    r -= 1
    g[l].append((r, d))
    g[r].append((l, -d))


def ok(cur: int, ds: int, dists: List[Optional[int]]) -> bool:
    dists[cur] = ds

    flag = True
    for nx, d in g[cur]:
        if dists[nx] != None:
            flag &= dists[nx] - dists[cur] == d
        elif flag:
            flag &= ok(nx, ds + d, dists)

    return flag


dists = [None] * N
ans = True
for i in range(N):
    if ans and dists[i] == None:
        ans &= ok(i, 0, dists)

print(("Yes" if ans else "No"))
