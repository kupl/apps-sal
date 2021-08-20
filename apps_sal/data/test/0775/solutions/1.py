(n, m, k) = list(map(int, input().split(' ')))
hs = list(map(int, input().split(' ')))
holes = set(hs)
pos = 1
for i in range(k):
    if pos in holes:
        break
    (u, v) = list(map(int, input().split(' ')))
    if pos == u:
        pos = v
    elif pos == v:
        pos = u
print(pos)
