import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n = int(input())
OP = [0] + list(map(int, input().split()))
f = list(map(int, input().split()))
CHLIST = [[] for i in range(n + 1)]
for i in range(n - 1):
    CHLIST[f[i]].append(i + 2)
LEAFLIST = []
for i in range(1, n + 1):
    if len(CHLIST[i]) == 0:
        LEAFLIST.append(i)
LEAF = len(LEAFLIST)
HEIGHT = [0] * (n + 1)
QUE = deque([1])
H = 1
while QUE:
    NQUE = deque()
    while QUE:
        x = QUE.pop()
        HEIGHT[x] = H
        for ch in CHLIST[x]:
            NQUE.append(ch)
    H += 1
    QUE = NQUE
LIST = list(range(1, n + 1))
LIST.sort(key=lambda x: HEIGHT[x], reverse=True)
NMINUS = [10] * (n + 1)


def node_minus(n):
    if NMINUS[n] != 10:
        return NMINUS[n]
    if len(CHLIST[n]) == 0:
        return 0
    if OP[n] == 1:
        ANS = -10 ** 7
        for ch in CHLIST[n]:
            ANS = max(ANS, node_minus(ch))
        NMINUS[n] = ANS
        return ANS
    else:
        ANS = 1
        for ch in CHLIST[n]:
            ANS -= 1
            ANS += node_minus(ch)
        NMINUS[n] = ANS
        return ANS


for l in LIST:
    node_minus(l)
print(LEAF + NMINUS[1])
