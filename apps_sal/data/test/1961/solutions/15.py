#!/usr/bin/env python3
import sys

def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()

def writable(r, c):
    if r+2 >= n or c+2 >= m:
        return False
    t = set()
    t.add(cells[r][c])
    t.add(cells[r][c+1])
    t.add(cells[r][c+2])
    t.add(cells[r+1][c])
    t.add(cells[r+1][c+2])
    t.add(cells[r+2][c])
    t.add(cells[r+2][c+1])
    t.add(cells[r+2][c+2])
    return not '.' in t

def fill_ink(r,c):
    paper[r][c] = "#"
    paper[r][c+1] = "#"
    paper[r][c+2] = "#"
    paper[r+1][c] = "#"
    paper[r+1][c+2] = "#"
    paper[r+2][c] = "#"
    paper[r+2][c+1] = "#"
    paper[r+2][c+2] = "#"

n, m = rint()

cells = []
for i in range(n):
    cells.append(input())

#for i in range(n):
#    for j in range(m):
#        print(cells[i][j], end='')
#    print()

paper = [["." for j in range(m)] for i in range(n)]

for r in range(n):
    for c in range(m):
        if writable(r,c) is True:
            fill_ink(r, c)

for r in range(n):
    for c in range(m):
        if cells[r][c] != paper[r][c]:
            print("NO")
            return

print("YES")

