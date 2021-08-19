(nr, nc, k) = map(int, input().strip().split())
total = 0
cols = [0] * nc
for r in range(nr):
    row = input().strip()
    for (i, e) in enumerate(row):
        if e == '*':
            total += max(0, cols[i] - k + 1)
            cols[i] = 0
        else:
            cols[i] += 1
    total += sum((max(0, len(s) - k + 1) for s in row.split('*') if s))
total += sum((max(0, x - k + 1) for x in cols))
if k == 1:
    total //= 2
print(total)
