from math import *


def bsearch(d, n):
    low = 0
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        val = mid + int(ceil(d / (mid + 1)))
        if val > n:
            high = mid - 1
        else:
            return True
    return False


def __starting_point():
    for _ in range(int(input())):
        n, d = list(map(int, input().split()))
        if bsearch(d, n):
            print("YES")
        else:
            print("NO")


__starting_point()
