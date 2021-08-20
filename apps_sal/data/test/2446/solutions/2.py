from sys import stdin
import math
from collections import defaultdict
input = stdin.readline
n = int(input())
arr = list(map(int, input().rstrip().split(' ')))
q = int(input())
d = defaultdict(lambda: 0)
current = defaultdict(lambda: 0)
for i in range(n):
    newCurrent = defaultdict(lambda: 0)
    newCurrent[arr[i]] += 1
    for (key, value) in current.items():
        g = math.gcd(arr[i], key)
        if g > 1:
            newCurrent[g] += value
    for (key, value) in newCurrent.items():
        d[key] += value
    current = newCurrent
totalCombi = n * (n + 1) // 2
d[1] = totalCombi - sum(d.values()) + arr.count(1)
for _ in range(q):
    x = int(input())
    print(d[x])
