
def main():
    buf = input()
    buflist = buf.split()
    h = int(buflist[0])
    w = int(buflist[1])
    S = []
    for i in range(h):
        buf = input()
        S.append(buf)
    cross_point = []
    for i in range(h):
        cross_point.append([])
        for j in range(w):
            if i > 0 and i < h-1 and j > 0 and j < w-1:
                if S[i][j] == '*' and S[i-1][j] == '*' and S[i+1][j] == '*' and S[i][j-1] == '*' and S[i][j+1] == '*':
                    cross_point[i].append(True)
                    continue
            cross_point[i].append(False)
    cross_point_location = None
    for i in range(h):
        for j in range(w):
            if cross_point[i][j]:
                if cross_point_location == None:
                    cross_point_location = (i, j)
                else:
                    print('NO') # multiple crosses
                    return
    if cross_point_location == None:
        print('NO') # no crosses
        return
    group = []
    for i in range(h):
        group.append([])
        for j in range(w):
            group[i].append(False)
    # down
    for i in range(cross_point_location[0], h):
        if S[i][cross_point_location[1]] == '*':
            group[i][cross_point_location[1]] = True
        else:
            break
    # up
    for i in range(cross_point_location[0], -1, -1):
        if S[i][cross_point_location[1]] == '*':
            group[i][cross_point_location[1]] = True
        else:
            break
    # right
    for j in range(cross_point_location[1], w):
        if S[cross_point_location[0]][j] == '*':
            group[cross_point_location[0]][j] = True
        else:
            break
    # left
    for j in range(cross_point_location[1], -1, -1):
        if S[cross_point_location[0]][j] == '*':
            group[cross_point_location[0]][j] = True
        else:
            break
    for i in range(h):
        for j in range(w):
            if S[i][j] == '*' and not group[i][j]:
                print('NO') # others are not empty
                return
    print('YES')


def __starting_point():
    main()

__starting_point()
