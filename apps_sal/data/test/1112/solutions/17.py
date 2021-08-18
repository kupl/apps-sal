
import sys

row1 = list(map(int, sys.stdin.readline().strip().split(' ')))
row2 = list(map(int, sys.stdin.readline().strip().split(' ')))
row3 = list(map(int, sys.stdin.readline().strip().split(' ')))
rows = [row1, row2, row3]

s1 = sum(row1)
s2 = sum(row2)
s3 = sum(row3)


def P(row, ix, num):
    if ix == 0:
        print('{} {} {}'.format(num, row[1], row[2]))
    elif ix == 1:
        print('{} {} {}'.format(row[0], num, row[2]))
    else:
        print('{} {} {}'.format(row[0], row[1], num))


z = (s2 + s1 - s3) // 2
y = s1 - z
x = s3 - y
vals = [x, y, z]

for ix, r in enumerate(rows):
    P(r, ix, vals[ix])

'''
T = x + y + z
y + z = sum(Row1)
x + z = sum(Row2)
x + y = sum(Row3)

'''
