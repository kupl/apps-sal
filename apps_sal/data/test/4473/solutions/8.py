import sys
from math import floor, ceil

input = sys.stdin.readline

t = int(input())

for zzz in range(t):
    r, l, k = list(map(int, input().split()))

    print(ceil(k/2)*r - floor(k/2)*l)

