import sys
import math

N, M = list(map(int, input().split()))

count = min(M//2, N)
M -= count*2
print(count + M//4)
