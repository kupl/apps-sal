from sys import stdin

n, m, k = list(map(int, stdin.readline().split()))
holes = set(map(int, stdin.readline().split()))

pos = 1
if pos not in holes:
    for i in range(k):
        u, v = list(map(int, stdin.readline().split()))
        if u == pos:
            pos = v
            if pos in holes:
                break
        elif v == pos:
            pos = u
            if pos in holes:
                break

print(pos)
