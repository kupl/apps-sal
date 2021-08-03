from math import sqrt

n, r = [int(x) for x in input().split()]

xcoords = [int(x) for x in input().split()]
ycoords = [-1 for x in xcoords]

for i, disk in enumerate(xcoords):
    maxy = r
    for j, disk2 in enumerate(xcoords):
        if disk2 < disk - 2 * r or disk2 > disk + 2 * r or ycoords[j] == -1:
            continue

        y = sqrt(pow(2 * r, 2) - pow(abs(disk2 - disk), 2)) + ycoords[j]

        if y > maxy:
            maxy = y

    ycoords[i] = maxy

s = ""
for disk in ycoords:
    s += str(disk) + " "

print(s[:-1])
