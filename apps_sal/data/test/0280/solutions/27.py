# -*- coding: utf-8 -*-

from sys import stdin
import math
import itertools
readline = stdin.readline
#n = int(readline())
#n, m = map(int, readline().split())
#a = list(map(int, readline().split()))
#l = [list(map(int, readline().split())) for _ in [0]*m]
n, m = list(map(int, readline().split()))
weights = list(map(int, readline().split()))

bridges = [list(map(int, readline().split())) for _ in [0]*m]
# 長さ順
bridges.sort()

# 長い順に橋の条件を見ていき、不要なものを取り除く処理
# 着目している橋Aについて、自分より長いかつ耐荷重が小さい橋Xが存在
# => Aの耐荷重条件はXの条件を満たせ自動的に満たされるので、Aは不要
bridges_filtered = []
bridges_filtered.append(bridges[m-1])
current_strongest_conditon_bridge = bridges[m-1]
bridges_filtered_len = 1
for i in range(m-2, -1, -1):
    bridge = bridges[i]
    if bridge[1] < current_strongest_conditon_bridge[1]:
        bridges_filtered.append(bridge)
        bridges_filtered_len += 1
        current_strongest_conditon_bridge = bridge

# ラクダ1頭で最も厳しい橋の耐荷重オーバーになるなら条件を満たすラクダ列は不可能
# 一番重いラクダ一頭だけ確認すれば十分
if current_strongest_conditon_bridge[1] < max(weights):
    print("-1")
    return


def acceptable_min_len(w):
    """
    重さwに耐えうる長さで最短のものを二分探索
    """
    l, r = 0, bridges_filtered_len - 1
    # bridges_filteredは長い順、耐荷重が大きい順となっている
    while l <= r:
        mid = (l+r)//2
        if bridges_filtered[mid][1] >= w:
            l = mid+1
        else:
            r = mid-1
    return bridges_filtered[l][0] if l <= bridges_filtered_len - 1 else 0


def min_len(seq):
    """
    seqはラクダの配列(並び替え済み)
    その配列で可能な最小の長さを返す
    """
    # dp[i]はi番目のラクダまで条件を満たすように並べた最小の長さ
    # dp[i] = iより前の全てのラクダとの区間において、橋をこわなさいような最小の長さを満たす
    dp = [0]*(n+1)
    # 重さの累積和。i-j番目のラクダの重さの総和を求めるのに使用
    cusum_wight = [0]
    for i in seq:
        cusum_wight.append(cusum_wight[-1]+weights[i])
    for i in range(2, n+1):
        for j in range(1, i):
            weight_between_i_j = cusum_wight[i]-cusum_wight[j-1]
            min_len_i_j = acceptable_min_len(weight_between_i_j)
            # 長いほうの条件を満たさないといけない
            dp[i] = max(dp[i], dp[j] + min_len_i_j)
    return dp[-1]


base = list(range(n))
combinations = itertools.permutations(base)
print((min(list(map(min_len, combinations)))))

