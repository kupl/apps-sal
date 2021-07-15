# 区間[i, j)
def checkAtomic(i, j):
    length = (j - i) // 2
    for k in range(i, (i + j) // 2):
        if A[k] == INF and A[k + length] is not None:
            return False
        if A[k] is not None and A[k] != INF and A[k] != k + length:
            return False

    for k in range((i + j) // 2, j):
        if A[k] == -1 and A[k - length] is not None:
            return False
        if A[k] is not None and A[k] != -1 and A[k] != k - length:
            return False

    return True

import sys
N = int(input())
floors = [[int(x) for x in input().split()] for _ in range(N)]
ON = 0;  OFF = 1;
INF = float('inf')
floors.sort()

ans = True
A = [None] * (2 * N + 1)

for on, off in floors:
    if on == -1 and off == -1:
        continue
    elif on == -1:
        if A[off] is not None:
            print('No')
            return
        A[off] = -1  # 乗った場所はわからない
        continue
    elif off == -1:
        if A[on] is not None:
            print('No')
            return
        A[on] = INF # 降りた場所はわからない
        continue
    elif on >= off:
        print('No')
        return
    elif (A[on] is not None) or (A[off] is not None):
        print('No')
        return
    else:
        A[on] = off
        A[off] = on



dp = [[0 for _ in range(2 * N + 2)] for _ in range(2 * N + 1)]

for length in range(2, 2 * N + 1, 2):
    for i in range(1, 2 * N + 2 - length):
        j = i + length
        dp[i][j] = sum(dp[i][k] * dp[k][j] for k in range(i + 2, j, 2)) + checkAtomic(i, j)
        res = dp[i][j]

if dp[1][2 * N + 1]:
    print('Yes')
else:
    print('No')
