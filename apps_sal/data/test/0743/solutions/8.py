from fractions import gcd
from functools import reduce

n = int(input())
nums = map(int, input().split())
print(reduce(lambda x, y: gcd(x, y), nums) * n)
