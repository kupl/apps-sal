#!/usr/bin python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
s = input()
s = s[::-1]
INF = 2 * n

if '1' * m in s:
    print(-1)
    return

dp = [-1] * (n + 1)
nw = 0
st = 0
nst = 0
ret = []
while nw < (n + 1):
    if s[nw] == '1':
        dp[nw] = INF
    else:
        dp[nw] = dp[st] + 1
        nst = nw
    nw += 1
    if nw == n + 1:
        ret.append(nst - st)
    elif nw > st + m:
        ret.append(nst - st)
        st = nst
print(' '.join(map(str, ret[::-1])))
