import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


for _ in range(int(input())):
    n, r = mapin()
    a = listin()
    a = list(set(a))
    a.sort()
    z = deque(a)
    count = 0
    while z:
        z.pop()
        count += 1
        if z:
            while z[0] <= r * count:
                z.popleft()
                if not z:
                    break
    print(count)
