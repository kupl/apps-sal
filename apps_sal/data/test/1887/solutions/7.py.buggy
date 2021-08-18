import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


n = getN()
anums = getList()
bnums = getList()

if n == 1:
    print(max(anums[0], bnums[0]))
    return

dp1 = [0 for i in range(n)]
dp2 = [0 for i in range(n)]

dp1[0] = anums[0]
dp1[1] = (anums[1] + bnums[0])
dp2[0] = bnums[0]
dp2[1] = (bnums[1] + anums[0])
i = 0
for a, b in (list(zip(anums[2:], bnums[2:]))):
    dp1[i + 2] = max(dp1[i], dp2[i + 1], dp2[i]) + a
    dp2[i + 2] = max(dp2[i], dp1[i + 1], dp1[i]) + b
    i += 1
print(max(dp1[-1], dp1[-2], dp2[-1], dp2[-2]))
# print(dp1)
# print(dp2)
