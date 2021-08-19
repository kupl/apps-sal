import math
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
low = 0
high = max(A)
while low <= high:
    if high == low:
        break
    mid = (low + high) // 2
    if mid == 0:
        break
    sum = 0
    for i in range(N):
        sum += math.ceil(A[i] / mid) - 1
    if sum > K:
        low = mid + 1
    else:
        high = mid
print(high)
