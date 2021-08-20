import math
from functools import reduce
l = int(input())
arr = list([int(x) for x in input().split(' ')])
cel = max(arr)
nwd = reduce(lambda x, y: math.gcd(x, y), [cel - x for x in arr])
people = sum(((cel - elem) // nwd for elem in arr))
print('{} {}'.format(people, nwd))
