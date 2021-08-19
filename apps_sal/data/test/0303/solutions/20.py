line1 = input()
line2 = input()
coords = list(map(int, line1.split()))
(v1, v2) = list(map(int, line2.split()))
dx = coords[2] - coords[0]
dy = coords[3] - coords[1]
if dx % v1 == 0 and dy % v2 == 0 and ((dx // v1 - dy // v2) % 2 == 0):
    print('YES')
else:
    print('NO')
