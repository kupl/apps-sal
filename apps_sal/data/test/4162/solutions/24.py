import math
from functools import reduce

n = int(input())
a_list = map(int, input().split())
result = 0
for a in a_list:
    result += a - 1 

print(result)
