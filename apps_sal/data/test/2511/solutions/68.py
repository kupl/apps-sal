import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LI2():
    return list(map(int, sys.stdin.readline().rstrip()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def LS2():
    return list(sys.stdin.readline().rstrip())


(N, K) = MI()
mod = 10 ** 9 + 7
Graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (a, b) = MI()
    Graph[a].append(b)
    Graph[b].append(a)
ans = K
for i in range(len(Graph[1])):
    ans *= K - i - 1
    ans %= mod
deq = deque([d for d in Graph[1]])
flag = [0] * (N + 1)
flag[1] = 1
for d in Graph[1]:
    flag[d] = 1
while deq:
    n = deq.pop()
    for i in range(len(Graph[n]) - 1):
        ans *= K - 2 - i
        ans %= mod
    for d in Graph[n]:
        if flag[d] == 0:
            flag[d] = 1
            deq.appendleft(d)
print(ans)
