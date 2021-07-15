#!/usr/bin/env python3

a, num = list(map(int, input().split()))

rows = {}
s = 0

for i in range(a):
    row = input()
    places = []
    best = []
    average = []

    for j, x in enumerate(row):
        if x == '.':
            row_ = ' ' + row + ' '
            if row_[j] != 'S' and row_[j + 2] != 'S':
                if num > 0:
                    row = row[:j] + 'x' + row[j+1:]
                    num -= 1
            elif row_[j] != 'S' or row_[j + 2] != 'S':
                average.append(j)
            else:
                places.append(j)

    rows[i] = {
        'average': average,
        'places': places,
        'row': row,
    }

for i in range(a):
    if rows[i]['average']:
        for j in rows[i]['average']:
            if num > 0:
                row = rows[i]['row']
                row = row[:j] + 'x' + row[j+1:]
                rows[i]['row'] = row
                num -= 1

for i in range(a):
    if rows[i]['places']:
        for j in rows[i]['places']:
            if num > 0:
                row = rows[i]['row']
                row = row[:j] + 'x' + row[j+1:]
                rows[i]['row'] = row
                num -= 1

for i in range(a):
    row = rows[i]['row']
    for j, x in enumerate(row):
        if x == 'S':
            row_ = ' ' + row + ' '
            if row_[j] in 'PSx':
                s += 1
            if row_[j + 2] in 'PSx':
                s += 1

print(s)

for i in range(a):
    print(rows[i]['row'])

