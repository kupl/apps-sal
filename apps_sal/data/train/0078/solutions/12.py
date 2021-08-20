from sys import stdin, stdout
import collections
import math
T = int(input())
for t in range(T):
    (N, M) = [int(x) for x in stdin.readline().split()]
    data = []
    row = [M] * N
    col = [N] * M
    for i in range(N):
        s = input()
        data.append(list(s))
        for j in range(M):
            if s[j] == '*':
                row[i] -= 1
                col[j] -= 1
    min_row = min(row)
    min_col = min(col)
    if min_row == 0 or min_col == 0:
        print(min_row + min_col)
    else:
        r = []
        c = []
        for i in range(N):
            if row[i] == min_row:
                r.append(i)
        for j in range(M):
            if col[j] == min_col:
                c.append(j)
        flag = 0
        for x in r:
            for y in c:
                if data[x][y] == '.' and flag == 0:
                    print(min_row + min_col - 1)
                    flag = 1
            if flag == 1:
                break
        if flag == 0:
            print(min_row + min_col)
