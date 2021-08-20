from functools import reduce
import math
(N, X) = map(int, input().split())
List = list(map(int, input().split()))
abs_List = [abs(List[i] - X) for i in range(N)]


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


print(gcd(*abs_List))
