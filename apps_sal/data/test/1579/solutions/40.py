N = int(input())
COR = [tuple(list(map(int, input().split()))) for _ in range(N)]


class Group:

    def __init__(self):
        self.n = 0
        self.x = 0
        self.y = 0
        self.xy = {}

    def new_cor_n(self):
        return self.x * self.y - self.n


def grouping(group, x, xcor, ycor):
    x_list = []
    group.x += 1
    for y in xcor[x][0]:
        if (x, y) not in group.xy:
            group.n += 1
            group.xy[x, y] = None
        if ycor[y][1]:
            continue
        ycor[y][1] = True
        group.y += 1
        for x_ in ycor[y][0]:
            if (x_, y) not in group.xy:
                group.n += 1
                group.xy[x_, y] = None
            if xcor[x_][1]:
                continue
            xcor[x_][1] = True
            x_list.append(x_)
    return x_list


if N <= 2:
    print(0)
else:
    (xcor, ycor) = ({}, {})
    for (xi, yi) in COR:
        if xi in xcor:
            xcor[xi][0].append(yi)
        else:
            xcor[xi] = [[yi], False]
        if yi in ycor:
            ycor[yi][0].append(xi)
        else:
            ycor[yi] = [[xi], False]
    group_list = []
    for (i, v) in list(xcor.items()):
        if v[1]:
            continue
        group = Group()
        group_list.append(group)
        xcor[i][1] = True
        x_list = [i]
        while True:
            new_x_list = []
            for x in x_list:
                new_x_list += grouping(group, x, xcor, ycor)
            if new_x_list == []:
                break
            x_list = new_x_list
    s = 0
    for group in group_list:
        s += group.new_cor_n()
    print(s)
