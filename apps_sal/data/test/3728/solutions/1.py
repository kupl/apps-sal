import sys


def swapC(c1, c2):
    for r in range(n):
        swap(r, c1, c2)


def swap(r, c1, c2):
    (nums[r][c1], nums[r][c2]) = (nums[r][c2], nums[r][c1])


def checkRow(r):
    bad = []
    for i in range(m):
        if nums[r][i] != i:
            bad.append(i)
    if len(bad) == 0:
        return True
    if len(bad) != 2:
        return False
    (x0, x1) = (nums[r][bad[0]], nums[r][bad[1]])
    return bad[0] == x1 and bad[1] == x0


def checkAll():
    for r in range(n):
        if not checkRow(r):
            return False
    return True


(n, m) = map(int, input().split())
nums = [list(map(lambda x: int(x) - 1, input().split())) for i in range(n)]
flag = False
for c1 in range(m):
    for c2 in range(c1, m):
        swapC(c1, c2)
        if checkAll():
            print('YES')
            flag = True
            break
        swapC(c1, c2)
    if flag:
        break
else:
    print('NO')
