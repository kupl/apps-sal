import sys


def get(p, x):
    path_x = []
    while x != p[x]:
        path_x.append(x)
        x = p[x]
    return x, path_x


def join(p, rank, x, y):
    x, path_x = get(p, x)
    y, path_y = get(p, y)

    if x == y:
        return False
    else:
        if rank[x] > rank[y]:
            x, y = y, x
        if rank[x] == rank[y]:
            rank[y] += 1

        p[x] = y
        for el in path_x:
            p[el] = y
        for el in path_y:
            p[el] = y
        return True


def check(p, x, y):
    x, path_x = get(p, x)
    y, path_y = get(p, y)

    for el in path_x:
        p[el] = x
    for el in path_y:
        p[el] = y
    return x == y


def get_id(c):
    return ord(c) - 97


reader = (s.rstrip() for s in sys.stdin)

n = int(next(reader))
p = list(range(26))
rank = [0] * 26
used = set()
for _ in range(n):
    word = next(reader)
    unq_cs = set(word)
    used.update(unq_cs)

    c1 = unq_cs.pop()
    i1 = get_id(c1)
    while unq_cs:
        c2 = unq_cs.pop()
        i2 = get_id(c2)
        join(p, rank, i1, i2)

unq_gr = set()
for c in used:
    gr_id, _ = get(p, get_id(c))
    unq_gr.add(gr_id)
print(len(unq_gr))
