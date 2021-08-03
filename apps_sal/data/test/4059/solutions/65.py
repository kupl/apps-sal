import math

N = int(input())

count = 0
for i in range(1, N):
    count += math.ceil(N / i) - 1

print(count)
