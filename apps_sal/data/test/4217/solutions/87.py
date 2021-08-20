import math
import collections
from itertools import product


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


(n, m) = mi()
ka = [li() for _ in range(n)]
food = [0] * m
for i in range(n):
    for j in range(1, ka[i][0] + 1, 1):
        food[ka[i][j] - 1] += 1
print(food.count(n))
