
"""
https://atcoder.jp/contests/arc085/tasks/arc085_c

"""

from collections import defaultdict
from collections import deque


def Ford_Fulkerson_Func(s, g, lines, cost):

    N = len(cost)
    ans = 0
    queue = deque([[s, float("inf")]])

    ed = [True] * N
    ed[s] = False

    route = [0] * N
    route[s] = -1

    while queue:

        now, flow = queue.pop()
        for nex in lines[now]:

            if ed[nex]:
                flow = min(cost[now][nex], flow)
                route[nex] = now
                queue.append([nex, flow])
                ed[nex] = False

                if nex == g:
                    ans += flow
                    break

        else:
            continue
        break

    else:
        return False, ans

    t = g
    s = route[t]

    while s != -1:
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)

        if cost[t][s] == 0:
            lines[t].add(s)
        cost[t][s] += flow
        t = s
        s = route[t]

    return True, ans


def Ford_Fulkerson(s, g, lines, cost):

    ans = 0

    while True:
        fl, nans = Ford_Fulkerson_Func(s, g, lines, cost)

        if fl:
            ans += nans
            continue
        else:
            break

    return ans


N = int(input())
a = list(map(int, input().split()))

S = N + 1
T = N + 2

lis = defaultdict(set)
cost = [[0] * (N + 3) for i in range(N + 3)]

for i in range(N):

    if a[i] > 0:
        lis[i + 1].add(T)
        cost[i + 1][T] += a[i]

    elif a[i] < 0:
        lis[S].add(i + 1)
        cost[S][i + 1] -= a[i]

for i in range(1, N + 1):

    for j in range(i * 2, N + 1, i):

        lis[i].add(j)
        cost[i][j] += float("inf")


m = Ford_Fulkerson(S, T, lis, cost)

ss = 0
for i in range(N):
    if a[i] > 0:
        ss += a[i]
print(ss - m)
