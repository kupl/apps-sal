(n, k) = list(map(int, input().split()))
rows = list()
nb = 0
places_by_nb = [list(), list(), list()]
for i in range(n):
    line = input()
    rows.append(list(line))
    row = '-%s-' % line
    for j in range(1, 13):
        if row[j] == 'S':
            if row[j - 1] == 'S' or row[j - 1] == 'P':
                nb += 1
            if row[j + 1] == 'S' or row[j + 1] == 'P':
                nb += 1
        elif row[j] == '.':
            t = 0
            if row[j - 1] == 'S':
                t += 1
            if row[j + 1] == 'S':
                t += 1
            places_by_nb[t].append((i, j - 1))
for m in range(0, 3):
    while k > 0 and len(places_by_nb[m]) > 0:
        place = places_by_nb[m].pop(-1)
        rows[place[0]][place[1]] = 'x'
        nb += m
        k -= 1
    if k == 0:
        break
print(nb)
for row in rows:
    print(''.join(row))
