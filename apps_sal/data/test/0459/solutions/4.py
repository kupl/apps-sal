a = [int(w) for w in input().split()]
cycles = [[5, 6, 17, 18, 21, 22, 13, 14], [9, 10, 19, 17, 4, 3, 14, 16], [8, 7, 16, 15, 24, 23, 20, 19], [7, 5, 3, 1, 22, 24, 11, 9], [6, 8, 10, 12, 23, 21, 2, 4], [18, 20, 12, 11, 15, 13, 1, 2]]
cycles = [[i - 1 for i in cycle] for cycle in cycles]
cycles += [list(reversed(cycle)) for cycle in cycles]


def rotate(a, cycle):
    b = a[:]
    for i in range(8):
        b[cycle[(i + 2) % 8]] = a[cycle[i]]
    return b


def ordered(a):
    for side in range(6):
        if not a[side * 4] == a[side * 4 + 1] == a[side * 4 + 2] == a[side * 4 + 3]:
            return False
    return True


for cycle in cycles:
    if ordered(rotate(a, cycle)):
        print('YES')
        break
else:
    print('NO')
