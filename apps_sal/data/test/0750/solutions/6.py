import sys
from math import floor, ceil

input = sys.stdin.readline

n, k = map(int, input().split())

print(ceil((n * 2) / k) + ceil((n * 5) / k) + ceil((n * 8) / k))
