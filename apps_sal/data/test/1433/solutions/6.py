(n, m) = map(int, input().split())
grid = [[i for i in map(int, input().split())] for _ in range(n)]
good_spots = 0
found1 = False
for row in grid:
    found1 = False
    if sum(row) == 0:
        continue
    last_one = len(row) - row[::-1].index(1) - 1
    for (idx, num) in enumerate(row):
        if num == 0:
            if idx < last_one:
                good_spots += 1
            if found1:
                good_spots += 1
        else:
            found1 = True
for c in range(m):
    found1 = False
    col = [row[c] for row in grid]
    if sum(col) == 0:
        continue
    last_one = len(col) - col[::-1].index(1) - 1
    for (idx, num) in enumerate(col):
        if num == 0:
            if idx < last_one:
                good_spots += 1
            if found1:
                good_spots += 1
        else:
            found1 = True
print(good_spots)
