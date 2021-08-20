import sys


def canMoveLeft(digit):
    index = [False, False, True, True, False, True, True, False, True, True]
    return index[digit]


def canMoveRight(digit):
    index = [False, True, True, False, True, True, False, True, True, False]
    return index[digit]


def canMoveUp(digit):
    index = [True, False, False, False, True, True, True, True, True, True]
    return index[digit]


def canMoveDown(digit):
    index = [False, True, True, True, True, True, True, False, True, False]
    return index[digit]


n = int(input())
number = [int(i) for i in input()]
movedown = [all([canMoveDown(i) for i in number]), all([canMoveUp(i) for i in number]), all([canMoveLeft(i) for i in number]), all([canMoveRight(i) for i in number])]
if any(movedown):
    print('NO')
else:
    print('YES')
