import sys


def canMoveLeft(digit):
    index = [
        False,  # 0
        False,  # 1
        True,  # 2
        True,  # 3
        False,  # 4
        True,  # 5
        True,  # 6
        False,  # 7
        True,  # 8
        True,  # 9
    ]
    return index[digit]


def canMoveRight(digit):
    index = [
        False,  # 0
        True,  # 1
        True,  # 2
        False,  # 3
        True,  # 4
        True,  # 5
        False,  # 6
        True,  # 7
        True,  # 8
        False,  # 9
    ]
    return index[digit]


def canMoveUp(digit):
    index = [
        True,  # 0
        False,  # 1
        False,  # 2
        False,  # 3
        True,  # 4
        True,  # 5
        True,  # 6
        True,  # 7
        True,  # 8
        True,  # 9
    ]
    return index[digit]


def canMoveDown(digit):
    index = [
        False,  # 0
        True,  # 1
        True,  # 2
        True,  # 3
        True,  # 4
        True,  # 5
        True,  # 6
        False,  # 7
        True,  # 8
        False,  # 9
    ]
    return index[digit]


n = int(input())
number = [int(i) for i in input()]
# print(number)

movedown = [all([canMoveDown(i) for i in number]),
            all([canMoveUp(i) for i in number]),
            all([canMoveLeft(i) for i in number]),
            all([canMoveRight(i) for i in number])]

if any(movedown):
    print('NO')
else:
    print('YES')

# print(movedown)
