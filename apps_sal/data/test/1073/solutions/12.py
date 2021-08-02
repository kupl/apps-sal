n = int(input())
d = [(0, 0)]
for c in input():
    dpos = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}[c]
    d.append((d[-1][0] + dpos[0], d[-1][1] + dpos[1]))
print(sum(1 for i in range(n) for j in range(i + 1, n + 1) if d[i] == d[j]))
