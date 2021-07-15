d = [{}, {}]
t = []

for i in range(8):
    x, y = [int(x) for x in input().split()]
    if [x, y] in t:
        print("ugly")
        return
    t.append([x, y])
    if x not in d[0]:
        d[0][x] = 1
    else:
        d[0][x] += 1
    if y not in d[1]:
        d[1][y] = 1
    else:
        d[1][y] += 1

if (len(d[0]) == 3) and (len(d[1]) == 3):
    a, b = [], []
    for k in sorted(d[0]):
        a.append(d[0][k])
    for k in sorted(d[1]):
        b.append(d[1][k])
    if (a == [3, 2, 3]) and (b == [3, 2, 3]):
        print("respectable")
    else:
        print("ugly")
else:
    print("ugly")

