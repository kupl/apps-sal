import math
N = int(input())
mod = 1000000007
x = [1 for _ in range(1001)]
Sum = 1

for i in range(1, N + 1):
    z = i
    for j in range(2, int(math.sqrt(N)) + 1):
        while z % j == 0:
            x[j] += 1
            z = int(z / j)
    if z != 1:
        x[z] += 1

for i in x:
    Sum *= i
    Sum %= mod

print(Sum)
