# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, K = LI()

# 逆に考える
"""
X = gcd(A_1, A_2,...A_K)
となるようなXを考えると溶ける
X = 3の時その個数は
[K/3]**N
"""

x_cnt = [0] * (K + 1)
for x in range(K, 0, -1):
    # print(x)
    tmp = pow(K // x, N, mod)
    for j in range(x + x, K+1, x):
        tmp -= x_cnt[j]
    x_cnt[x] = tmp

ans = 0
for i in range(1,K+1):
    ans += i * x_cnt[i]
    ans %= mod
print(ans)


    


