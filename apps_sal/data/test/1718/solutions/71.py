import math
n, k = map(int, input().split())
A = list(map(int, input().split()))

A_min = min(A)
N = n-len([i for i in A if i == A_min])
print(math.ceil(N/(k-1)))
