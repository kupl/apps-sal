import math
n = int(input())
nums = [int(input()) for _ in range(5)]
min_n = math.ceil(n / min(nums))
print(4 + min_n)
