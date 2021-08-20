import math
(d, g) = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(d)]
ans = sum([i[0] for i in p])
for i in range(2 ** d - 1):
    bit = bin(i)[2:].zfill(d)
    (c, s, a) = (0, 0, 0)
    for j in range(d):
        if bit[j] == '1':
            c += p[j][0]
            s += p[j][1] + 100 * (j + 1) * p[j][0]
        else:
            a = max(a, j)
    short = g - s
    pc = max(math.ceil(short / ((a + 1) * 100)), 0)
    if pc < p[a][0]:
        ans = min(c + pc, ans)
print(ans)
