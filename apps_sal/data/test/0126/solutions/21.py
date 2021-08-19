input()
a = list(map(int, str(input())))
d = {1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (0, 1), 5: (1, 1), 6: (2, 1), 7: (0, 2), 8: (1, 2), 9: (2, 2), 0: (1, 3)}
r = list(map(lambda x: (d[x][0] + 1, d[x][1]), a))
l = list(map(lambda x: (d[x][0] - 1, d[x][1]), a))
t = list(map(lambda x: (d[x][0], d[x][1] + 1), a))
b = list(map(lambda x: (d[x][0], d[x][1] - 1), a))
rt = list(map(lambda x: (d[x][0] + 1, d[x][1] + 1), a))
rb = list(map(lambda x: (d[x][0] + 1, d[x][1] - 1), a))
lt = list(map(lambda x: (d[x][0] - 1, d[x][1] + 1), a))
lb = list(map(lambda x: (d[x][0] - 1, d[x][1] - 1), a))
if all([x in d.values() for x in r]) or all([x in d.values() for x in l]) or all([x in d.values() for x in t]) or all([x in d.values() for x in b]) or all([x in d.values() for x in rt]) or all([x in d.values() for x in rb]) or all([x in d.values() for x in lt]) or all([x in d.values() for x in lb]):
    print('NO')
else:
    print('YES')
