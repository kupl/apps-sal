from sys import stdin, stdout
import math
from math import gcd, sqrt
N = int(input())
arr = [int(x) for x in stdin.readline().split()]
add = [-1, 0, 1]
arr.sort()
freq = {}
res = 0
for i in range(N):
    for j in range(3):
        w = arr[i] + add[j]
        if w > 0 and w not in freq:
            freq[w] = 1
            res += 1
            break
print(res)
