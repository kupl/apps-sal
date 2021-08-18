import math
from bisect import bisect_left
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


inf = 10 ** 10
n, x, y = getList()
nums = getList()
nums = [inf] * x + nums + [inf] * y
# print(nums)
for i in range(n):
    flag = 0
    tgt = nums[x + i]
    # print(tgt)
    for j in range(x):
        dif = nums[x + i - j - 1]
        # print(dif)
        if dif <= tgt:
            flag = 1
            continue
    if not flag:
        for j in range(y):
            dif = nums[x + i + j + 1]
            # print(dif)
            if dif <= tgt:
                flag = 1
                continue

    # print(flag)
    if not flag:
        print(i + 1)
        return
