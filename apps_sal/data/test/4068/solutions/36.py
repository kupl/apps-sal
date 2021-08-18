"""
Created on Sun Sep 13 12:06:59 2020

@author: liang
"""


key = 10**9 + 7
N, M = map(int, input().split())

A = [int(input()) for _ in range(M)]
A.sort()
A += [-1]


def solve():
    steps = list()
    count = 0
    index = 0
    for i in range(N + 1):
        if i == A[index]:
            if count == 0:
                return 0
            else:
                steps.append(count)
                count = 0
                if index < M:
                    index += 1
        else:
            count += 1
    else:
        steps.append(count)
        count = 0

    smax = max(steps)
    fibs = [0] * smax
    for i in range(smax):
        if i == 0 or i == 1:
            fibs[i] = 1
        else:
            fibs[i] = fibs[i - 1] + fibs[i - 2]
    else:
        ans = 1
        for s in steps:
            ans *= fibs[s - 1]
            ans %= key
    return ans


ans = solve()
print(ans)
