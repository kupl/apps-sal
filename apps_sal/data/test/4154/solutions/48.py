from itertools import accumulate
N, M = list(map(int, input().split()))

left = 1
right = N

for i in range(M):
    a, b = list(map(int, input().split()))
    left = max(left, a)
    right = min(right, b)

print((max(0, right - left + 1)))
