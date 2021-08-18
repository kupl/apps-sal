#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc068/tasks/abc068_b
import math


def fact(N):
    ans = {}
    for i in range(2, math.ceil(math.sqrt(N)) + 1):
        if N % i != 0:
            continue
        ex = 0

        while N % i == 0:
            ex += 1
            N /= i
        ans[i] = ex

    if N != 1:
        ans[int(N)] = 1
    return ans


N = int(input())
max_x = 0
max_n = 0

if N == 1:
    print((1))
    return

for i in range(N + 1):
    num = fact(i)
    num = num.get(2, 0)
    if num > max_n:
        max_x = i
        max_n = num

print(max_x)
