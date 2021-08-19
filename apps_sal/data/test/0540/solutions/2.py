#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test(x):
    if x == 'X' or type(x) == int:
        return False
    return True


(n, m) = (int(i) for i in input().split())
map = []

for i in range(n):
    map.append([i for i in input()])

for i in map:
    while ' ' in i:
        i.remove(' ')


(r1, c1) = (int(i) for i in input().split())
(r2, c2) = (int(i) for i in input().split())

step = 0
map[r1 - 1][c1 - 1] = 0

if (map[r2 - 1][c2 - 1] == 'X'):
    flag = 0
    map[r2 - 1][c2 - 1] = '.'
else:
    flag = 1

now = [(r1 - 1, c1 - 1)]

while (type(map[r2 - 1][c2 - 1]) != int and now != []):
    now_new = []
    for (i, j) in now:
        if (i > 0):
            if test(map[i - 1][j]):
                map[i - 1][j] = step + 1
                now_new.append((i - 1, j))
        if (i < n - 1):
            if test(map[i + 1][j]):
                map[i + 1][j] = step + 1
                now_new.append((i + 1, j))

        if (j > 0):
            if test(map[i][j - 1]):
                map[i][j - 1] = step + 1
                now_new.append((i, j - 1))

        if (j < m - 1):
            if test(map[i][j + 1]):
                map[i][j + 1] = step + 1
                now_new.append((i, j + 1))

    now = now_new
    step = step + 1

if (type(map[r2 - 1][c2 - 1]) != int):
    print("NO")

else:
    if flag == 0:
        print("YES")
    else:
        acc = 0
        acc1 = 0
        i = r2 - 1
        j = c2 - 1

        if (i > 0):
            if type(map[i - 1][j]) == int:
                acc1 += 1
            elif map[i - 1][j] != 'X':
                acc += 1

        if (i < n - 1):
            if type(map[i + 1][j]) == int:
                acc1 += 1
            elif map[i + 1][j] != 'X':
                acc += 1

        if (j > 0):
            if type(map[i][j - 1]) == int:
                acc1 += 1
            elif map[i][j - 1] != 'X':
                acc += 1

        if (j < m - 1):
            if type(map[i][j + 1]) == int:
                acc1 += 1
            elif map[i][j + 1] != 'X':
                acc += 1

        if (acc == 0 and acc1 < 2):
            print("NO")
        else:
            print("YES")
