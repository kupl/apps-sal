# -*- coding: utf-8 -*-

def check(H, W, s, x, y):
    res = False
    if x - 1 >= 0 and s[y][x-1] == '#':
        res = True
    if x + 1 < W and s[y][x+1] == '#':
        res = True
    if y - 1 >= 0 and s[y-1][x] == '#':
        res = True
    if y + 1 < H and s[y+1][x] == '#':
        res = True

    return res


H,W = map(int, input().split())
s = []
for h in range(H):
    s.append(list(input()))

for y in range(H):
    for x in range(W):
        if s[y][x] == "#" and not check(H, W, s, x, y):
            print("No")
            return

print("Yes")
