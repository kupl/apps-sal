def list_int():
    return list(map(int, input().split()))


def int_in():
    return int(input())


def map_in():
    return list(map(int, input().split()))


def list_in():
    return input().split()


t = int_in()
for _ in range(t):
    v = set()
    s = input()
    x = 0
    y = 0
    c = 0
    for i in s:
        if i == 'N':
            if (x, y, x + 1, y) in v:
                c += 1
            elif (x + 1, y, x, y) in v:
                c += 1
            else:
                c += 5
            v.add((x, y, x + 1, y))
            x += 1
        elif i == 'S':
            if (x, y, x - 1, y) in v:
                c += 1
            elif (x - 1, y, x, y) in v:
                c += 1
            else:
                c += 5
            v.add((x, y, x - 1, y))
            x -= 1
        elif i == 'W':
            if (x, y, x, y + 1) in v:
                c += 1
            elif (x, y + 1, x, y) in v:
                c += 1
            else:
                c += 5
            v.add((x, y, x, y + 1))
            y += 1
        else:
            if (x, y, x, y - 1) in v:
                c += 1
            elif (x, y - 1, x, y) in v:
                c += 1
            else:
                c += 5
            v.add((x, y, x, y - 1))
            y -= 1
    print(c)
