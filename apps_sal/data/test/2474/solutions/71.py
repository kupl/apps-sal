import itertools
import sys
N = int(input())
C = [int(x) for x in input().split()]
C.sort()
sum = 0
for i in range(N):
    sum += (N + 1 - i) * C[i]
sum *= 2 ** (N - 2)
sum *= 2 ** N
print(int(sum % (10 ** 9 + 7)))
