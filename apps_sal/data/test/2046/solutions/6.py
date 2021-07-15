from heapq import *

N = int(input().strip())
snacks = [int(x) for x in input().strip().split(' ')]

snacks_sorted = sorted(snacks)

buffer = []

for i in range(N):
    heappush(buffer, -snacks[i])
    while len(buffer) > 0 and -buffer[0] == snacks_sorted[-1]:
        snacks_sorted.pop()
        x = heappop(buffer)
        print(-x,"",end="")
    print()


