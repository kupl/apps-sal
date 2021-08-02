import math
N = int(input())
A = list(map(int, input().split()))

A = list(map(lambda x: int(math.copysign(x - 1, x)), A))

print(sum(A))
