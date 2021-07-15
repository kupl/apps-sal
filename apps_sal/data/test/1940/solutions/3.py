from sys import stdin
import math

N, K = list(map(int, stdin.readline().split()))
pebbles = list(map(int, stdin.readline().split()))

print(math.ceil(sum(math.ceil(p / K) for p in pebbles) / 2))

