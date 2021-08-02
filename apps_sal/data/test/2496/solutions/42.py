# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 07:10:00 2020

@author: liang
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 00:26:07 2020

@author: liang
"""

"""
コーナーケース１:
    重複があるとき　not coprime
    ただし、1の重複は除く
"""
import math
C = 10**6
N = int(input())
judge = [False] * (C + 1)
A = [int(x) for x in input().split()]

f = True
for a in A:
    if judge[a] == True and a != 1:
        f = False
    judge[int(a)] = True


# print(judge[:10])
def solve(f):

    ans = A[0]
    # 線形探索 O(N)
    for i in range(N):
        ans = math.gcd(ans, A[i])
    # print("ans",a)
    if ans != 1:
        return "not coprime"

    flag = True
    # エラトステネスの篩 O(N log N)
    for i in range(2, C + 1):
        count = 0
       # if d[i] == True:
        for j in range(i, C + 1, i):
            if judge[j] == True:
                count += 1
            if count == 2:
                flag = False
                break
        #        d[j] = False
        if not flag:
            break

    if flag == True and f == True:
        return "pairwise coprime"

    return "setwise coprime"


print((solve(f)))
# print(len(A))
