import math
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
mini = 0
maxi = max(A)
while maxi - mini > 1:
    mid = (maxi + mini) // 2
    s = sum((math.ceil(a / mid) - 1 for a in A))
    if s > K:
        mini = mid
    else:
        maxi = mid
print(mini + 1)
