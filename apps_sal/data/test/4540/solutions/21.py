from copy import deepcopy
n = int(input())
A = list(map(int, input().split()))
B = [0] + deepcopy(A) + [0]
total = 0
b = 0
for a in A:
    total += abs(a - b)
    b = a
total += abs(b)
for i in range(1, n + 1):
    (z, x, c) = (B[i - 1], B[i], B[i + 1])
    print(total - abs(x - z) - abs(c - x) + abs(c - z))
