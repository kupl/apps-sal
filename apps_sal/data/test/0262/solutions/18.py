from collections import defaultdict
import sys
import os
import math


def __starting_point():
    n = int(input())
    s = [list(map(int, input().split())) for i in range(n)]
    if n == 1:
        print(1)
        return
    pos = []
    for i in range(n):
        for j in range(n):
            if s[i][j] == 0:
                pos = [i, j]
                break
    val = sum(s[(pos[0] + 1) % n])
    s[pos[0]][pos[1]] = max(val - sum(s[pos[0]]), 1)
    for i in range(n):
        if sum(s[i]) != val:
            print(-1)
            return
    for j in range(n):
        t = 0
        for i in range(n):
            t += s[i][j]
        if t != val:
            print(-1)
            return
    t, tt = 0, 0
    for i in range(n):
        t += s[i][i]
        tt += s[i][n - 1 - i]
    if t != val or tt != val:
        print(-1)
        return

    print(s[pos[0]][pos[1]])
    '''
    for i in range(n):
        print(' '.join(map(str, s[i])))
    '''


__starting_point()
