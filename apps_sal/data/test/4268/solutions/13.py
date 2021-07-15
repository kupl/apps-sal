from typing import List
from math import sqrt


def distance(x1: List[int], x2: List[int]) -> float:
    total = 0
    for a, b in zip(x1, x2):
        total += (a - b) ** 2
    return sqrt(total)


nd = list(map(int, input().split()))
n, d = nd[0], nd[1]
xs = [list(map(int, input().split())) for _ in range(n)]
size = len(xs)
result = 0

for i in range(size):
    for j in range(i + 1, size):
        if distance(xs[i], xs[j]).is_integer():
            result += 1

print(result)

