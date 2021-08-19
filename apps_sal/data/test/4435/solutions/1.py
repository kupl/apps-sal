import sys
from itertools import chain, permutations
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(' ')))
result = [-1 for _ in a]
jumps_to = [[] for _ in a]
for i in range(len(a)):
    left = i - a[i]
    right = i + a[i]
    if left >= 0:
        jumps_to[left].append(i)
        if a[left] % 2 != a[i] % 2:
            result[i] = 1
    if right < n:
        jumps_to[right].append(i)
        if a[right] % 2 != a[i] % 2:
            result[i] = 1
queue = []
queue_ptr = 0
for i in range(n):
    if result[i] == 1:
        queue.append(i)
while queue_ptr < len(queue):
    current = queue[queue_ptr]
    for to in jumps_to[current]:
        if result[to] == -1 or result[to] > result[current] + 1:
            queue.append(to)
            result[to] = result[current] + 1
    queue_ptr += 1
print(' '.join(map(str, result)))
