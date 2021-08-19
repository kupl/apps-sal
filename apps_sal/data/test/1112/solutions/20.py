rows = [list(map(int, input().split())) for x in range(3)]
(a, b, c, d) = (rows[0][2], rows[1][2], rows[1][0], rows[2][0])
sums = [c + d, a + d, a + b]
s = sum(sums) // 2
for x in range(3):
    rows[x][x] = s - sums[x]
for x in rows:
    print(' '.join(map(str, x)))
