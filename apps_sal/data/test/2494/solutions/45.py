from collections import deque
import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)


def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


k = ni()
que = deque([(1, 1)])

kmod = [0] * k

while kmod[0] == 0:
    cost, idx = que.popleft()
    if kmod[idx] == 0:
        kmod[idx] = cost
        que.appendleft((cost, (10 * idx % k)))
        que.append((cost + 1, (idx + 1) % k))

print(kmod[0])
