# 桁DP練習
# 「0以外の値をkより多く使ったか」でとくに枝切りしてない
# ループでどうしてもかけない...

from sys import setrecursionlimit

setrecursionlimit(10**7)

n = input()
k = int(input())
dp = {}


def rec(i, smaller, count):
    if (i, smaller, count) in dp:
        return dp[(i, smaller, count)]
    if i == len(n):
        if count == k:
            return 1
        else:
            return 0
    limit = 10
    if not smaller:
        limit = int(n[i]) + 1
    ret = 0
    for j in range(limit):
        if smaller or j < int(n[i]):
            if j == 0:
                ret += rec(i + 1, True, count)
            else:
                ret += rec(i + 1, True, count + 1)
        else:
            if j == 0:
                ret += rec(i + 1, False, count)
            else:
                ret += rec(i + 1, False, count + 1)
    dp[(i, smaller, count)] = ret
    return ret


print((rec(0, False, 0)))
