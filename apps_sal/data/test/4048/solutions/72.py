import math
N = int(input())
result = N
for i in range(1, int(math.sqrt(N))+2):
    if N % i == 0:
        result = min(result, i - 1 + N//i - 1)
print(result)

