import sys
from collections import *


def arr_inp(n):
    return [int(x) for x in sys.stdin.readline().split()]


def up():
    nonlocal ans
    mi, c = pos[1], 0
    for i in range(pos[0], n + 1):
        mi = min(mi, cols[i - 1] + 1)

        if i == pos[2]:
            ans = min(ans, pos[2] - pos[0] + abs(mi - pos[3]))
        elif i > pos[2]:
            if pos[2] < pos[0]:
                ans = min(ans, (pos[0] - pos[2]) + (2 * c) + abs(min(min(cols[pos[2] - 1:pos[0]]) + 1, mi) - pos[3]))
            else:
                ans = min(ans, (i - pos[2]) + c + abs(min(min(cols[pos[0]:i]) + 1, mi) - pos[3]))

        c += 1


def down():
    nonlocal ans
    mi, c = pos[1], 1
    for i in range(pos[0] - 1, 0, -1):
        mi = min(mi, cols[i - 1] + 1)

        if i == pos[2]:
            ans = min(ans, pos[0] - pos[2] + abs(mi - pos[3]))
        elif i < pos[2]:
            if pos[2] >= pos[0]:
                ans = min(ans, (pos[2] - pos[0]) + (2 * c) + abs(min(min(cols[pos[0] - 1:pos[2]]) + 1, mi) - pos[3]))
            else:
                ans = min(ans, (pos[2] - i) + c + abs(min(min(cols[i:pos[0]]) + 1, mi) - pos[3]))

        c += 1


sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
n, cols, pos = int(sys.stdin.readline()), arr_inp(1), arr_inp(1)
ans = float('inf')
up()
down()
print(ans)

