import math
ln, cl = (int(x) for x in input().split())

in_dt = []

for i in range(ln):
    in_dt.append(input())


def is_adj(x_1, y_1, x_2, y_2):
    if math.abs(x_2 - x_1) == 1 and y_2 - y_1 == 0:
        return True
    elif math.abs(y_2 - y_1) == 1 and x_2 - x_1 == 0:
        return True
    return False


ch_dt = [[0 for x in range(55)] for y in range(55)]


def neighb(x, y, ln, cl, lst):
    res = []
    if x - 1 >= 0 and lst[x][y] == lst[x - 1][y]:
        res.append((x - 1, y))
    if y - 1 >= 0 and lst[x][y] == lst[x][y - 1]:
        res.append((x, y - 1))
    if x + 1 < ln and lst[x][y] == lst[x + 1][y]:
        res.append((x + 1, y))
    if y + 1 < cl and lst[x][y] == lst[x][y + 1]:
        res.append((x, y + 1))
    return res


path = []


def go_path(lst, path):
    nonlocal ln
    nonlocal cl
    while True:
        if len(path) == 0:
            break
        cur_x = path[-1][0]
        cur_y = path[-1][1]
        del path[-1]
        #print (cur_x, cur_y)
        #print (path)
        neighbours = neighb(cur_x, cur_y, ln, cl, lst)
        # print(neighbours)
        if len(neighbours) != 0:
            for neighbour in neighbours:
                if neighbour in path:
                    return True
                # print ("_______")
                #print (ch_dt)
                #print (neighbour)
                #print ("+++++++")
                if ch_dt[neighbour[0]][neighbour[1]] == 0:
                    path.append(neighbour)
                    ch_dt[neighbour[0]][neighbour[1]] = 1
        # print(path)
    #print (False)
    return False


for i in range(ln):
    for j in range(cl):
        if ch_dt[i][j] == 0:
            ch_dt[i][j] = 1
            path.append((i, j))
            if go_path(in_dt, path):
                print("Yes")
                return
print("No")
