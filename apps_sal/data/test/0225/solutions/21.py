a1, a2, a3, a4 = map(int, input().split())

res = False

for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                if (i1*a1 + i2*a2 + i3*a3 + i4*a4)*2 == a1 + a2 + a3 + a4:
                    res = True

if res:
    print('YES')
else:
    print('NO')
