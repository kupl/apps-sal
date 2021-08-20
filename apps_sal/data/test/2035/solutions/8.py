(n, sx, sy) = input().split()
(n, sx, sy) = (int(n), int(sx), int(sy))
(cl, cr, cu, cd) = (0, 0, 0, 0)
for i in range(n):
    (xi, yi) = input().split()
    (xi, yi) = (int(xi), int(yi))
    if xi < sx:
        cl += 1
    if xi > sx:
        cr += 1
    if yi < sy:
        cd += 1
    if yi > sy:
        cu += 1
mx = max([cl, cr, cu, cd])
print(mx)
if mx == cl:
    print(str(sx - 1) + ' ' + str(sy))
elif mx == cr:
    print(str(sx + 1) + ' ' + str(sy))
elif mx == cd:
    print(str(sx) + ' ' + str(sy - 1))
elif mx == cu:
    print(str(sx) + ' ' + str(sy + 1))
