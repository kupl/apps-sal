from math import floor, ceil

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pos = dict()
    for p, i in enumerate(a):
        pos[i] = p
    minpos = [None] + [pos[1]] + [None] * (n - 1)
    maxpos = [None] + [pos[1]] + [None] * (n - 1)

    for i in range(2, n + 1):
        minpos[i] = min(minpos[i - 1], pos[i])
        maxpos[i] = max(maxpos[i - 1], pos[i])

    good = ['0'] * n
    for i in range(1, n + 1):
        if maxpos[i] - minpos[i] + 1 == i:
            good[i - 1] = '1'

    print(''.join(good))
