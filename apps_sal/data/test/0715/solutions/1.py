a = []
for i in range(4):
    x = input().strip()[2:]
    a.append(len(x))
good = []
for i in range(4):
    fl = True
    for j in range(4):
        if j != i and a[i] / a[j] < 2:
            fl = False
    if fl:
        good.append(i)
    else:
        fl = True
        for j in range(4):
                if j != i and a[j] / a[i] < 2:
                    fl = False 
        if fl:
            good.append(i)
if len(good) == 1:
    print(chr(ord('A') + good[0]))
else:
    print('C')
