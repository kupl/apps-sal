n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
bh = [0] * n
c = [0] * n
for (i, s) in enumerate(f):
    for (j, h) in enumerate(s):
        bh[i] |= h << j
maxp = -float('inf')
for mbh in range(1, 2 ** 10):
    for i in range(n):
        intsect = mbh & bh[i]
        c[i] = sum((intsect >> k & 1 for k in range(10)))
    maxp = max(maxp, sum((p[i][c[i]] for i in range(n))))
print(maxp)
