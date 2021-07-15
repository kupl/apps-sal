pole = [[], [], [], [], [], [], [], [], []]
for i in range(3):
        for k in range(3):
                a = input().split()
                pole[i * 3].append(a[0])
                pole[i * 3 + 1].append(a[1])
                pole[i * 3 + 2].append(a[2])
        k = input()
k = list(map(int, k.split()))
i1 = (k[0] - 1) % 3
i2 = (k[1] - 1) % 3
ix = i1 * 3 + i2
if '.' not in ''.join(pole[ix]):
        for i in range(9):
                for k in range(3):
                        n = ''
                        for l in list(pole[i][k]):
                                if l == '.':
                                        n += '!'
                                else:
                                        n += l
                        pole[i][k] = n
else:
        for i in range(3):
                n = ''
                for l in list(pole[ix][i]):
                        if l == '.':
                                n += '!'
                        else:
                                n += l
                pole[ix][i] = n                        
for i in range(3):
        for k in range(3):
                print(pole[i * 3][k], pole[i * 3 + 1][k], pole[i * 3 + 2][k])
        print()

