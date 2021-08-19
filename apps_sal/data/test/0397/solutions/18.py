import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def validation(n, k, x):
    if x * (x + 1) // 2 - (n - x) == k:
        return 0
    if x * (x + 1) // 2 - (n - x) > k:
        return 1
    return 2


(n, k) = getList()
l = 0
r = 1000000001
while True:
    mid = (l + r) // 2
    flag = validation(n, k, mid)
    if flag == 0:
        ans = mid
        break
    elif flag == 1:
        r = mid
    else:
        l = mid
print(n - ans)
