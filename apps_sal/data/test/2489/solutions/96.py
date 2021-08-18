"""
Created on Sat Sep 12 00:21:05 2020

@author: liang
"""

N = int(input())
A = [int(x) for x in input().split()]

A.sort()
A += [-1]
dp = [0] + [True] * 10**6


def Solve():
    if A[0] == 1:
        if len(A) >= 2 and A[1] == 1:
            return 0
        else:
            return 1
    k = 0
    for i in range(1, 10**6 + 1):
        if i == A[k]:
            tmp = A[k]
            cnt = 0
            while k <= N - 1 and A[k] == tmp:
                cnt += 1
                if cnt == 2:
                    dp[tmp] = False
                k += 1
            for j in range(2 * i, 10**6 + 1, i):
                dp[j] = False
    ans = 0
    for a in A[:-1]:
        if dp[a]:
            ans += 1
    return ans


ans = Solve()
print(ans)
