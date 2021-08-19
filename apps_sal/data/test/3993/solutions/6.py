(n, m, k) = list(map(int, input().split(' ')))
p = tuple(map(int, input().split(' ')))
d = 0
part = (p[0] - 1) // k
moves = 0
skip = 0
for pi in p:
    if (pi - 1 - d) // k == part:
        skip += 1
        continue
    d += skip
    part = (pi - 1 - d) // k
    skip = 1
    moves += 1
print(moves + 1)
