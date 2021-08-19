n = int(input())
c = [0, 0]
ans = []
for i in range(n):
    (minx, miny) = (c[0], c[1])
    (v, x, y) = input().split()
    (x, y) = (int(x), int(y))
    (x, y) = (max(x, y), min(x, y))
    if v == '+':
        if not (x <= minx and y <= miny or (x <= miny and y <= minx)):
            if x > minx:
                if y > minx:
                    minx = y
                    if x > miny:
                        miny = x
                else:
                    minx = x
                    if y > miny:
                        miny = y
            elif y > miny:
                miny = y
    elif x >= minx and y >= miny or (x >= miny and y >= minx):
        ans.append('YES')
    else:
        ans.append('NO')
    c = sorted([minx, miny], reverse=True)
print('\n'.join(ans))
