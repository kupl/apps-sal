#!/usr/bin/env python3
import copy

n = int(input())

mod = 10**9 + 7

memo = {}

banned = {'ACTG', 'TCAG', 'GCAG', 'TACG', 'AACG', 'ACAG', 'GAGC', 'CACG',
          'AGC', 'ATCG', 'ACCG', 'CAG', 'GACG', 'CCAG', 'AAGC', 'ACG', 'TAGC'}

count = 0


def dp(lettrs, state):

    if state in banned:
        return 0
    if lettrs == 0:
        return 1
    if (lettrs, state) in memo:
        return memo[lettrs, state]

    ans = 0
    for c in "ACGT":
        ans += dp(lettrs - 1, (state + c)[-4:])
        ans %= mod
    ans %= mod
    memo[lettrs, state] = ans

    return ans


print((dp(n, "")))
# print(memo)
# AG = [0, 1]
# for i in range(2, n):
#     ans_pre = copy.deepcopy(ans)
#     ans = copy.deepcopy(ans_base)
#     print(ans_pre)
#     for key in ans_pre.keys():

#         for l in ["A", "C", "G", "T"]:

#             if key+l in miss:
#                 print(key+l)
#                 continue
#             else:
#                 # print((key+l))
#                 ans[(key+l)[1:]] += ans_pre[key] % mod
#     AG.append(ans["AG"])
#     print(AG)
#     ans["AC"] -= AG[-3]
#     ans["GC"] -= AG[-3]
#     ans["TC"] -= AG[-3]


# print(sum(ans.values()) % mod)

# AA
# AC
# AG
# AT
# CA
# CC
# CG
# CT
# GA
# GC
# GG
# GT
# TA
# TC
# TG
# TT
