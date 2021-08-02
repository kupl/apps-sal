n = int(input())

l = [41, 10, 11, 12, 20, 21, 22, 30, 31, 32]
s = list([l[int(x)] for x in input()])


def exists_up(s):
    l1 = [x - 10 for x in s]
    return all(x in l for x in l1)


def exists_down(s):
    l1 = [x + 10 for x in s]
    return all(x in l for x in l1)


def exists_left(s):
    l1 = [x - 1 for x in s]
    return all(x in l for x in l1)


def exists_right(s):
    l1 = [x + 1 for x in s]
    return all(x in l for x in l1)


if exists_up(s) or exists_down(s) or exists_left(s) or exists_right(s):
    print("NO")
else:
    print("YES")
