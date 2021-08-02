from collections import defaultdict
import math

n = int(input().lstrip())
numbers = []

for _ in range(n):
    numbers.append(list(map(int, input().lstrip().split())))


def gcd(a, b):
    if not a:
        return b
    return gcd(b % a, a)


slope_map = defaultdict(set)
total = 0
res = 0
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = numbers[i]
        x2, y2 = numbers[j]
        a = y1 - y2
        b = x1 - x2
        d = gcd(a, b)
        a //= d
        b //= d
        if a < 0 or (not a and b < 0):
            a *= -1
            b *= -1
        slope = (a, b)
        c = a * x1 - b * y1
        if c not in slope_map[slope]:
            total += 1
            slope_map[slope].add(c)
            res += total - len(slope_map[slope])
print(res)
