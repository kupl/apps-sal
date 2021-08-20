import math
N = int(input())
A = [int(i) for i in input().split()]
left = [0] * (N + 1)
for i in range(1, N + 1):
    left[i] = math.gcd(left[i - 1], A[i - 1])
right = [0] * (N + 1)
right[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    right[i] = math.gcd(right[i + 1], A[i])
output = 0
for i in range(N):
    output = max(output, math.gcd(left[i], right[i + 1]))
print(output)
