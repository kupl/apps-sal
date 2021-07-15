#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc074/tasks/abc074_b

N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0
for x in X:
    if x > abs(K-x):
        ans += abs(K-x)*2
    else:
        ans += x*2
print(ans)

