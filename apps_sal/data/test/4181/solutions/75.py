from collections import deque
from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if A[i] >= B[i]:
        cnt += B[i]
    else:
        cnt += A[i]
        d = B[i] - A[i]
        if d <= A[i + 1]:
            cnt += d
            A[i + 1] -= d
        else:
            cnt += A[i + 1]
            A[i + 1] = 0
print(cnt)
