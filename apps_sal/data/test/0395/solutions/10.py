l = list(map(int, input().split()))
t = False
for i1 in range(6):
    for i2 in range(i1 + 1, 6):
        for i3 in range(i2 + 1, 6):
            if l[i1] + l[i2] + l[i3] == sum(l) - (l[i1] + l[i2] + l[i3]):
                t = True
if t == True:
    print('YES')
else:
    print('NO')
