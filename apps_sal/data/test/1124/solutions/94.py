import math


def multi_gcd(lst):
    if len(lst) == 1:
        return lst[0]
    gcd = 0
    for i in range(1, len(lst)):
        if i == 1:
            gcd = math.gcd(lst[0], lst[1])
        else:
            gcd = math.gcd(gcd, lst[i])
    return gcd


n = int(input())
a = list(map(int, input().split()))
print(multi_gcd(a))
