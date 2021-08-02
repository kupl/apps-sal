import sys
from collections import Counter
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = Counter(arr)
keys = sorted(d.keys())

res = 0
max = 0

for i in range(len(keys)):
    while(d[keys[i]] > 0):
        if d[keys[i]] > 3:
            d[keys[i]] = 3
        d[keys[i]] -= 1
        if max < keys[i] - 1:
            max = keys[i] - 1
            res += 1
        elif max == keys[i] - 1:
            max = keys[i]
            res += 1
        elif max == keys[i]:
            max = keys[i] + 1
            res += 1

print(res)
