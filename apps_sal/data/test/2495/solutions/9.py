# coding:UTF-8
import sys

MOD = 10 ** 9 + 7
INF = float('inf')

N = int(input())    # 数字
A = list(map(int, input().split()))     # スペース区切り連続数字

res1 = 0
res2 = 0

s = 0
for i in range(N):
    s = s + A[i]
    if i % 2 == 1 and s <= 0:
        shift = -s + 1
        s += shift
        res1 += shift
    if i % 2 == 0 and s >= 0:
        shift = s + 1
        s -= shift
        res1 += shift

s = 0
for i in range(N):
    s = s + A[i]
    if i % 2 == 0 and s <= 0:
        shift = -s + 1
        s += shift
        res2 += shift
    if i % 2 == 1 and s >= 0:
        shift = s + 1
        s -= shift
        res2 += shift

print(("{}".format(min(res1, res2))))

