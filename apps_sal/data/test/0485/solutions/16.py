from collections import defaultdict
n = int(input())
dx = defaultdict(int)
dy = defaultdict(int)
mx = my = 0
lx = ly = 100
s = set()
for i in range(4 * n + 1):
    (x, y) = list(map(int, input().split()))
    s.add((x, y))
    dx[x] += 1
    dy[y] += 1
    if dx[x] > 1:
        if x > mx:
            mx = x
        if x < lx:
            lx = x
    if dy[y] > 1:
        if y > my:
            my = y
        if y < ly:
            ly = y
for el in s:
    if lx < el[0] < mx and ly < el[1] < my or el[0] < lx or el[0] > mx or (el[1] < ly) or (el[1] > my):
        print(*el)
