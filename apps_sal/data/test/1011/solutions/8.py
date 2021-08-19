(n, _a) = (int(input()), list(map(int, input().split())))
(m, _b) = (int(input()), list(map(int, input().split())))
p = [(ai, 0) for ai in _a] + [(bi, 1) for bi in _b]
p.sort()
i = 0
R = [len(_a) * 3, len(_b) * 3]
r = list(R)
while i < len(p):
    d = p[i][0]
    while i < len(p) and p[i][0] == d:
        r[p[i][1]] -= 1
        i += 1
    if r[0] - r[1] > R[0] - R[1]:
        R = list(r)
print(*R, sep=':')
