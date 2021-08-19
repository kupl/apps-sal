import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, d, a) = list(map(int, input().split()))
    XH = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    que = deque()
    total = 0
    res = 0
    for i in range(n):
        (x, h) = XH[i]
        while que and que[0][0] < x:
            total -= que[0][1]
            que.popleft()
        h -= total
        if h > 0:
            num = (h + a - 1) // a
            res += num
            damage = num * a
            total += damage
            que.append([x + d * 2, damage])
    print(res)


def __starting_point():
    resolve()


__starting_point()
