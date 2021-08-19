import math
from collections import defaultdict
import sys


def arr():
    return list(map(int, input().split()))


input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    L = arr()
    L.sort()
    flag = False
    for i in range(1, 1025):
        x = L[:]
        for j in range(N):
            x[j] = x[j] ^ i
        x.sort()
        x.sort()
        if x == L:
            ans = i
            flag = True
            break
    if flag:
        print(ans)
    else:
        print(-1)
