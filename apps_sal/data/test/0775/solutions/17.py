import sys

n, m, k = list(map(int, sys.stdin.readline().strip().split(" ")))

holes = set(map(int, sys.stdin.readline().strip().split(" ")))

pos = 1
for i in range(k):
    u, v = list(map(int, sys.stdin.readline().strip().split(" ")))

    if pos not in holes:
        if pos == u:
            pos = v
        elif pos == v:
            pos = u

print(pos)
