class Coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def cdist(c1, c2):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


(x1, y1) = list(map(int, input().split()))
(x2, y2) = list(map(int, input().split()))
(x3, y3) = list(map(int, input().split()))
cs = [Coord(x1, y1), Coord(x2, y2), Coord(x3, y3)]
s = set()
s.add(tuple([x1, y1]))
s.add(tuple([x2, y2]))
s.add(tuple([x3, y3]))
shifts = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(3):
    cur = cs[i]
    other = []
    for j in range(3):
        if j != i:
            other.append(cs[j])
    cur_x = cur.x
    cur_y = cur.y
    while True:
        cnt = 0
        for sh in shifts:
            (new_x, new_y) = (cur_x + sh[0], cur_y + sh[1])
            flag = 0
            for oth in other:
                (oth_x, oth_y) = (oth.x, oth.y)
                if dist(cur_x, cur_y, oth_x, oth_y) > dist(new_x, new_y, oth_x, oth_y):
                    pass
                else:
                    flag += 1
            if flag:
                cnt += 1
                continue
            s.add(tuple([new_x, new_y]))
            (cur_x, cur_y) = (new_x, new_y)
            break
        if cnt == 4:
            break
arr = list(s)
print(len(arr))
for a in arr:
    print(*a)
