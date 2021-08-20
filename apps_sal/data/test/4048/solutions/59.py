import math
N = int(input())
x = N + 1
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        x = min(x, i + N // i)
print(x - 2)
