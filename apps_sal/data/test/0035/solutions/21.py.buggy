n, m = list(map(int, input().split()))
field = [input() for i in range(n)]

if n % 3 == 0:
    size = n // 3
    flag = True
    block = set()
    stripes = set()
    for i in range(n):
        if i % size == 0:
            block = set()
        for j in range(m):
            block.add(field[i][j])
        if (i + 1) % size == 0:
            if len(block) > 1:
                flag = False
            else:
                stripes.add(list(block)[0])
    if len(stripes) != 3:
        flag = False
    if flag:
        print('YES')
        return

if m % 3 == 0:
    size = m // 3
    flag = True
    block = set()
    stripes = set()
    for j in range(m):
        if j % size == 0:
            block = set()
        for i in range(n):
            block.add(field[i][j])
        if (j + 1) % size == 0:
            if len(block) > 1:
                flag = False
            else:
                stripes.add(list(block)[0])
    if len(stripes) != 3:
        flag = False
    if flag:
        print('YES')
        return

print('NO')
