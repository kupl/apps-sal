"""
Created on Tue Sep 22 16:34:00 2020

@author: liang
"""

N = int(input())
A = [0] + [int(x) for x in input().split()] + [0]
ans = 0
for i in range(N + 1):
    ans += abs(A[i + 1] - A[i])

for i in range(1, N + 1):
    tmp = ans
    if A[i - 1] <= A[i] <= A[i + 1]:
        print(tmp)
    elif A[i - 1] >= A[i] >= A[i + 1]:
        print(tmp)
    else:
        tmp -= min(abs(A[i] - A[i - 1]), abs(A[i + 1] - A[i])) * 2
        print(tmp)
