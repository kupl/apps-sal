import sys

N, M = [int(i) for i in input().split()]
map = {k: [] for k in range(1, N + 1)}

for _ in range(M):
    a, b = (int(i) for i in input().split())
    map[a].append(b)


for i in map[1]:
    if N in map[i]:
        print('POSSIBLE')
        return


print('IMPOSSIBLE')
