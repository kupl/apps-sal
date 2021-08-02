from bisect import bisect_right
import sys
import os
import io
input = sys.stdin.readline
N, K = map(int, input().split())
A = [-float('inf')] + list(map(int, input().split())) + [float('inf')]
if K:
    B = [0] + list(map(int, input().split())) + [N + 1]
else:
    B = [0, N + 1]
ans = N - K
for k in range(K + 1):
    left, right = B[k], B[k + 1]
    if A[left] - left > A[right] - right:
        print(-1)
        break
    lis = []
    for i in range(left + 1, right):
        if not A[left] - left <= A[i] - i <= A[right] - right:
            continue
        ind = bisect_right(lis, A[i] - i)
        if ind == len(lis):
            lis.append(A[i] - i)
        else:
            lis[ind] = A[i] - i
    ans -= len(lis)
else:
    print(ans)
