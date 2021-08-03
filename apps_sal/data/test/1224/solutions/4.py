import math

N = int(input())

Amax = math.ceil(18 / math.log10(3))
Bmax = math.ceil(18 / math.log10(5))
# print(Amax,Bmax)

for A in range(1, Amax + 1):
    for B in range(1, Bmax + 1):
        if 3**A + 5**B == N:
            print(A, B)
            return

print(-1)
