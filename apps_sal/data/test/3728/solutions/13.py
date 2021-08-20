from sys import stdin
(n, m) = (int(x) for x in stdin.readline().split())
table = []
for _ in range(n):
    table.append([int(x) for x in stdin.readline().split()])


def tr(l):
    return list(map(list, list(zip(*l))))


def need_one_or_zero_swap(l):
    swap = 2
    for (i, item) in enumerate(l):
        if item != i + 1:
            if swap:
                if l[item - 1] == i + 1:
                    swap -= 1
                else:
                    return False
            else:
                return False
    return True


def check_after_global_swap(t):
    for row in t:
        if not need_one_or_zero_swap(row):
            return False
    return True


def try_global_swap_first():
    if check_after_global_swap(table):
        return True
    transp = tr(table)
    for i in range(len(transp)):
        for j in range(i + 1, len(transp)):
            (transp[i], transp[j]) = (transp[j], transp[i])
            t2 = tr(transp)
            if check_after_global_swap(t2):
                return True
            (transp[i], transp[j]) = (transp[j], transp[i])
    return False


if try_global_swap_first():
    print('YES')
else:
    print('NO')
