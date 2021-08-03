
"""

答えがX未満になる場合の数がわかればおk
→距離がX以上となるすべての点対間において違う色で塗られている

直径を考えてみる
端点を白とするとからX以上の距離は全て黒
もう片方の端点からX以上の距離は全て白にぬる
当然かぶったらout

かぶらなかったらok?
仮定する

実装は
各Xに関して、両方からX以内の頂点の数を数え上げる

"""

import sys
from sys import stdin

# 重みのないグラフでの最短経路問題
#隣接リストと始点を与えると始点からの距離のリスト & 親のリストを返す
from collections import deque


def NC_Dij(lis, start):

    ret = [float("inf")] * len(lis)
    ret[start] = 0

    q = deque([start])
    plis = [i for i in range(len(lis))]

    while len(q) > 0:
        now = q.popleft()

        for nex in lis[now]:

            if ret[nex] > ret[now] + 1:
                ret[nex] = ret[now] + 1
                plis[nex] = now
                q.append(nex)

    return ret, plis


mod = 10**9 + 7

N = int(stdin.readline())

lis = [[] for i in range(N)]

for i in range(N - 1):
    a, b = list(map(int, stdin.readline().split()))
    a -= 1
    b -= 1
    lis[a].append(b)
    lis[b].append(a)

D0, tmp = NC_Dij(lis, 0)
p1 = 0
for i in range(N):
    if D0[i] > D0[p1]:
        p1 = i

D1, tmp = NC_Dij(lis, p1)
p2 = p1
for i in range(N):
    if D1[i] > D1[p2]:
        p2 = i

D2, tmp = NC_Dij(lis, p2)

DL1 = []
for i in range(N):
    DL1.append((D1[i], i))
DL2 = []
for i in range(N):
    DL2.append((D2[i], i))

DL1.sort()
DL1.reverse()
DL2.sort()
DL2.reverse()


anslis = [0] * N
visit = [0] * N
two = 0
zero = N
for X in range(N):

    while len(DL1) > 0 and DL1[-1][0] == X:
        tmp, v = DL1[-1]
        del DL1[-1]

        if visit[v] == 0:
            zero -= 1
        elif visit[v] == 1:
            two += 1
        visit[v] += 1

    while len(DL2) > 0 and DL2[-1][0] == X:
        tmp, v = DL2[-1]
        del DL2[-1]

        if visit[v] == 0:
            zero -= 1
        elif visit[v] == 1:
            two += 1
        visit[v] += 1

    if two == N:
        anslis[X] = pow(2, N, mod)
    elif zero == 0:
        anslis[X] = 2 * pow(2, two, mod)

ans = 0
for i in range(1, N):
    ans += (anslis[i] - anslis[i - 1]) * i
print((ans % mod))
