import math
import statistics
N = int(input())
A = [int(x) for x in input().split()]
avg = math.floor(statistics.mean(A))
a = 0
b = 0
for i in range(len(A)):
    a += (A[i] - avg) ** 2
    b += (A[i] - avg - 1) ** 2
print(min(a, b))
