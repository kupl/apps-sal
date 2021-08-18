import sys
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
n = int(input())
s = input()

us = s.count('U')
ds = s.count('D')
ls = s.count('L')
rs = s.count('R')


rlswap = False
udswap = False
if x2 < x1:
    # L <-> R
    rlswap = True
    ls, rs = rs, ls
if y2 < y1:
    # D -> U
    udswap = True
    us, ds = ds, us
# We're going top right

dx = abs(x1 - x2)
dy = abs(y1 - y2)
# if ds == n or ls == n:
#    print(-1)
#    return


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


wx = rs - ls
wy = us - ds

dstart = dist(0, 0, dx, dy)
dawind = dist(wx, wy, dx, dy)

free = n

l = 0
r = (dx + dy + 1) * n
while r - l > 1:
    t = (l + r) // 2
    if dist(*(wx * t, wy * t), dx, dy) > free * t:
        l = t
    else:
        r = t

t = l
t = max(0, t - 1)
count = n * t

x = wx * t
y = wy * t
free = free * t

for c in s * 10:
    if dist(x, y, dx, dy) <= free:
        break
    if c in 'RL' and rlswap:
        c = 'RL'[c == 'R']
    if c in 'UD' and udswap:
        c = 'UD'[c == 'U']

    if c == 'U':
        y += 1
    if c == 'D':
        y -= 1
    if c == 'L':
        x -= 1
    if c == 'R':
        x += 1

    free += 1
    count += 1
else:
    print(-1)
    return

print(count)
