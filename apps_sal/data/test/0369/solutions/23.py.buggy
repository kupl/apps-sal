import sys
N, M = list(map(int, input().split()))
S = [int(c) for c in input()][::-1]

c = 0
path = []
while c < N:
    g = c + M if c + M < N else N
    for m in range(g, c, -1):
        if S[m] == 1:
            continue
        else:
            path.append(m - c)
            c = m
            break
    else:
        if c < N:
            print((-1))
            return

print((*path[::-1]))
