import itertools
import math

N = int(input())
p = []
for i in range(N):
    x, y = [int(n) for n in input().split()]
    p.append([x, y])

total_length = 0
k = 0
for pattern in itertools.permutations(p):
    k += 1
    length = 0
    for i in range(N-1):
        length += math.sqrt((pattern[i+1][0] - pattern[i][0])**2 + (pattern[i+1][1] - pattern[i][1])**2)
    total_length += length

print(total_length/k)
