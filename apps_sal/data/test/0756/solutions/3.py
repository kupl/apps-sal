import math
from collections import Counter

def solve():
    n = int(input())
    T = [int(x) for x in input().split()]
    time = 0
    for t in T:
        if t > min(time + 15, 90):
            return min(time + 15, 90)
        else:
            time = t
    return min(time + 15, 90)

print(solve())


