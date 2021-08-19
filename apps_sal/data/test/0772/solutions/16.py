l = []
for i in range(3):
    l1 = input().split()
    for j in range(3):
        l1[j] = int(l1[j])
    l.append(l1)
for i in range(3):
    for j in range(3):
        c = l[i][j]
        if i > 0:
            c += l[i - 1][j]
        if j > 0:
            c += l[i][j - 1]
        if i < 2:
            c += l[i + 1][j]
        if j < 2:
            c += l[i][j + 1]
        if c % 2 == 0:
            print(1, end='')
        else:
            print(0, end='')
    print()
