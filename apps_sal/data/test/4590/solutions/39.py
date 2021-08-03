from itertools import accumulate
import bisect

N, M, K = map(int, input().split())
A = [0] + list(accumulate(map(int, input().split())))
B = [0] + list(accumulate(map(int, input().split())))

X = 0
Y_num = [0] * (N + 1)

for i in range(N + 1):
    if A[i] <= K:
        X = bisect.bisect_right(B, K - A[i])
        Y_num[i] = i + X - 1

print(max(Y_num))
