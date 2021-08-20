import math


def min_perimeter(n):
    sq = math.floor(math.sqrt(n))
    rem = n - sq ** 2
    if rem == 0:
        return sq * 4
    elif rem <= sq:
        return sq * 4 + 2
    else:
        return sq * 4 + 4


n = int(input())
print(min_perimeter(n))
