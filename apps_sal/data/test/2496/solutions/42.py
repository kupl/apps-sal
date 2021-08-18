"""
Created on Fri Sep 18 07:10:00 2020

@author: liang
"""


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


def solve(f):

    ans = A[0]
    for i in range(N):
        ans = math.gcd(ans, A[i])
    if ans != 1:
        return "not coprime"

    flag = True
    for i in range(2, C + 1):
        count = 0
        for j in range(i, C + 1, i):
            if judge[j] == True:
                count += 1
            if count == 2:
                flag = False
                break
        if not flag:
            break

    if flag == True and f == True:
        return "pairwise coprime"

    return "setwise coprime"


print((solve(f)))
