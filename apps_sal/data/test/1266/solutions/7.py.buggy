n = int(input())

x, y = map(int, input().split())

directions = [None for x in range(8)]
# u, ur, r, rd, d, dl, l, lu

for i in range(n):
    line = input().split()
    xi = int(line[1])
    yi = int(line[2])

    if yi == y:
        if xi < x:
            # left
            if directions[6] == None:
                directions[6] = (xi, yi, line[0])
            elif directions[6][0] < xi:
                directions[6] = (xi, yi, line[0])
        else:
            # right
            if directions[2] == None:
                directions[2] = (xi, yi, line[0])
            elif directions[2][0] > xi:
                directions[2] = (xi, yi, line[0])
    elif xi == x:
        if yi < y:
            # down
            if directions[4] == None:
                directions[4] = (xi, yi, line[0])
            elif directions[4][1] < yi:
                directions[4] = (xi, yi, line[0])
        else:
            # up
            if directions[0] == None:
                directions[0] = (xi, yi, line[0])
            elif directions[0][1] > yi:
                directions[0] = (xi, yi, line[0])
    elif xi - x == yi - y:
        if xi > x:
            # upright
            if directions[1] == None:
                directions[1] = (xi, yi, line[0])
            elif directions[1][0] > xi:
                directions[1] = (xi, yi, line[0])
        else:
            # downleft
            if directions[5] == None:
                directions[5] = (xi, yi, line[0])
            elif directions[5][1] < yi:
                directions[5] = (xi, yi, line[0])
    elif xi - x == y - yi:
        if xi > x:
            # rightdown
            if directions[3] == None:
                directions[3] = (xi, yi, line[0])
            elif directions[3][0] > xi:
                directions[3] = (xi, yi, line[0])
        else:
            # leftup
            if directions[7] == None:
                directions[7] = (xi, yi, line[0])
            elif directions[7][1] > yi:
                directions[7] = (xi, yi, line[0])

for i in range(8):
    if directions[i] != None:
        if i % 2 == 0:
            if directions[i][2] == "R" or directions[i][2] == "Q":
                print("YES")
                return
        else:
            if directions[i][2] == "B" or directions[i][2] == "Q":
                print("YES")
                return

print("NO")
