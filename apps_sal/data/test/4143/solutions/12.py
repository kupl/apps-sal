import math
N = int(input())
mobile = [int(input()) for _ in range(5)]

res = math.ceil(N / min(mobile)) + 4

print(res)
