n, m = map(int, input().split())
a = []
start = None
for i in range(n):
    s = input()
    a.append(s)
    if 'S' in s:
        start = [i, s.index('S')]
h = input()
ans = 0
ms = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def check(d):
    ps = [i for i in start]
    for l in h:
        nm = ms[d[int(l)]]
        dx, dy = nm
        ps = [ps[0] + dx, ps[1] + dy]
        if ps[0] >= n or ps[0] < 0 or ps[1] < 0 or ps[1] >= m or a[ps[0]][ps[1]] == '#':
            return False
        if a[ps[0]][ps[1]] == 'E':
            return True
    return False


for i in range(4):
    for j in range(4):
        if j != i:
            for k in range(4):
                if k not in [i, j]:
                    for z in range(4):
                        if z not in [i, j, k]:
                            if check({0: i, 1: j, 2: k, 3: z}):
                                ans += 1
print(ans)
