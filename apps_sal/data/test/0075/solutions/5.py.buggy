R, C = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(R)]

wpr = [0] * R
wpc = [0] * C
n = 0

for r in range(R):
    for c in range(C):
        if grid[r][c] != '*':
            continue
        wpr[r] += 1
        wpc[c] += 1
        n += 1

for r in range(R):
    for c in range(C):
        field = 1 if grid[r][c] == '*' else 0

        if wpr[r] + wpc[c] - field == n:
            print('YES')
            print(r + 1, c + 1)
            return

print('NO')
