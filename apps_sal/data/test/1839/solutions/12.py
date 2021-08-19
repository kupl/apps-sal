import sys
lines = iter(sys.stdin.read().split('\n'))
n = int(next(lines))
rows = [0] * (n + 1)
cols = [0] * (n + 1)
res = []
for i in range(n ** 2):
    (r, c) = list(map(int, next(lines).strip(' ').split(' ')))
    if rows[r] == 0 and cols[c] == 0:
        rows[r] = 1
        cols[c] = 1
        res.append(str(i + 1))
print(' '.join(res))
