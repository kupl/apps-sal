(n, sx, sy) = map(int, input().split())
b = [0] * 4
'\n    |\n    1\n---2-0---\n    3\n    |\n'
for i in range(n):
    (x, y) = map(int, input().split())
    if sy == y:
        if sx < x:
            b[0] += 1
        else:
            b[2] += 1
    elif sx == x:
        if sy < y:
            b[1] += 1
        else:
            b[3] += 1
    elif sx < x:
        b[0] += 1
        if sy < y:
            b[1] += 1
        else:
            b[3] += 1
    elif sx > x:
        b[2] += 1
        if sy < y:
            b[1] += 1
        else:
            b[3] += 1
a = max(b)
print(a)
i = b.index(a)
if i == 0:
    print(sx + 1, sy)
elif i == 1:
    print(sx, sy + 1)
elif i == 2:
    print(sx - 1, sy)
else:
    print(sx, sy - 1)
