MOVS = [(2, -2), (-2, 2), (-2, -2), (2, 2)]


def check(a):
    return 0 <= a < 8


set1 = set()
set2 = set()
dic1 = dict()
dic2 = dict()


def cango1(matrix, pos, lap):
    for dx, dy in MOVS:
        nx, ny = dx + pos[0], dy + pos[1]
        if not check(nx) or not check(ny):
            continue
        if (nx, ny) in set1:
            continue
        dic1[(nx, ny)] = lap % 2
        set1.add((nx, ny))
        cango1(matrix, (nx, ny), lap + 1)


def cango2(matrix, pos, lap):
    for dx, dy in MOVS:
        nx, ny = dx + pos[0], dy + pos[1]
        if not check(nx) or not check(ny):
            continue
        if (nx, ny) in set2:
            continue
        dic2[(nx, ny)] = lap % 2
        set2.add((nx, ny))
        cango2(matrix, (nx, ny), lap + 1)


q = int(input())
for ww in range(q):
    matrix = [input().strip() for i in range(8)]
    pos = []
    bad = set()
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 'K':
                pos.append((i, j))
            if matrix[i][j] == '#':
                bad.add((i, j))
    set1, set2, dic1, dic2 = set(), set(), dict(), dict()
    cango1(matrix, pos[0], 0)
    cango2(matrix, pos[1], 0)
    if ww != q - 1:
        input()
    sec = (set1 & set2) - bad
    for x, y in sec:
        if dic1[(x, y)] == dic2[(x, y)]:
            print("YES")
            break
    else:
        print("NO")
