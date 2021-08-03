import math

N = int(input())

min_cost = N - 1

for i in range(1, int(math.sqrt(N)) + 1):
    tmp = 0
    if N % i == 0:
        tmp = (i - 1) + (N / i - 1)
        if tmp < min_cost:
            min_cost = tmp
print(int(min_cost))
