import sys
from collections import deque
sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり
def LI2(): return list(map(int, sys.stdin.readline().rstrip()))  # 空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  # 空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  # 空白なし


N, Q = MI()
Graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = MI()
    Graph[a].append(b)
    Graph[b].append(a)

count = [0] * (N + 1)
add_count = [0] * (N + 1)
for i in range(Q):
    p, x = MI()
    add_count[p] += x

flag = [-1] * (N + 1)
count[1] = add_count[1]
deq = deque([(1, add_count[1])])
flag[1] = 0

while deq:
    n, r = deq.pop()
    for d in Graph[n]:
        if flag[d] == -1:
            flag[d] = 0
            count[d] = r + add_count[d]
            deq.appendleft((d, count[d]))

print((*count[1:]))
