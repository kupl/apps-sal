import math
from collections import Counter
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


n, k = getList()


stu = []
for i in range(n):
    d = getN()
    stu.append(d)

cnt = Counter(stu)
ans = 0
for v in cnt.values():
    ans += (v // 2) * 2

ans += (n - ans + 1) // 2

print(ans)
