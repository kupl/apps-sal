import math
N = int(input())
A = [int(input()) for _ in range(5)]
a = min(A)
print(math.ceil(N / a) + 4)
