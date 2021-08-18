n = int(input())
s = input().rstrip()


def canMove(moves, dx, dy):
    for x, y in moves:
        tx = x + dx
        ty = y + dy
        if not (0 <= tx < 3 and 0 <= ty < 3):
            if not (tx == 3 and ty == 1):
                return False
    return True


l = [
    [	3, 1, ],
    [	0, 0, ],
    [	0, 1, ],
    [	0, 2, ],
    [	1, 0, ],
    [	1, 1, ],
    [	1, 2, ],
    [	2, 0],
    [	2, 1, ],
    [	2, 2, ],
]


move = []
for x in s:
    move.append(l[int(x)])

cnt = 0
for i in range(10):
    for j in range(10):
        dx = i - 5
        dy = j - 5
        if canMove(move, dx, dy):
            cnt += 1
if cnt == 1:
    print('YES')
else:
    print('NO')
