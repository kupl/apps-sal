from sys import stdin

n, k = list(map(int, stdin.readline().rstrip().split()))
data = stdin.readline().rstrip()

doors = {}
for c in data:
    if c in doors:
        doors[c] += 1
    else:
        doors[c] = 1

opening_doors_count = 0
opened_doors = {}

for c in data:
    if c not in opened_doors:
        opened_doors[c] = True
        opening_doors_count += 1

    if opening_doors_count > k:
        print('YES')
        return

    doors[c] -= 1

    if doors[c] == 0:
        opening_doors_count -= 1
        opened_doors[c] = False

print('NO')

