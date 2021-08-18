#!/usr/bin/env python3
import sys


def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()


n = int(input())

s = (input())

l_cnt = 1
for i in range(1, n):
    if s[i] == s[0]:
        l_cnt += 1
    else:
        break
r_cnt = 1
for i in range(n - 2, -1, -1):
    if s[i] == s[-1]:
        r_cnt += 1
    else:
        break

if l_cnt == n:
    print((n * (n + 1) // 2) % 998244353)
    return

if s[0] == s[-1]:
    print((l_cnt + 1) * (r_cnt + 1) % 998244353)
    return

print(1 + r_cnt + l_cnt)
