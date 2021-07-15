coords = {0: (1, 0), 1: (0, 3), 2: (1, 3), 3: (2, 3), 4: (0, 2), 5: (1, 2), 6: (2, 2), 7: (0, 1), 8: (1, 1), 9: (2, 1)}
valid_coords = set()
for elem in coords:
    valid_coords.add(coords[elem])
n = input()
s = [int(elem) for elem in input()]
vectors = []
for i in range(len(s) - 1):
    t = [0, 0]
    t[0] = coords[s[i + 1]][0] - coords[s[i]][0]
    t[1] = coords[s[i + 1]][1] - coords[s[i]][1]
    vectors.append(t)
cnt = 0
for elem in coords:
    start = coords[elem]
    faults = 0
    for v in vectors:
        new_start = (start[0] + v[0], start[1] + v[1])
        start = new_start
        if start not in valid_coords:
            faults += 1
    if faults == 0:
        cnt += 1
if cnt == 1:
    print('YES')
else:
    print('NO')
