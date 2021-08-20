import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


ipnut = input
q = int(input())
for i in range(q):
    (h, n, m) = list(map(int, input().split()))
    while n and h > 20:
        h = h // 2 + 10
        n -= 1
    while m and h > 0:
        h -= 10
        m -= 1
    if h > 0:
        print('NO')
    else:
        print('YES')
