n = int(input())

ludia = []
for i in range(n):
    s = input().split()
    ludia.append([s[0], int(s[1]), int(s[2])])

maxi = 0
for den in range(1, 367):
    muzov, zien = 0, 0
    for clovek in ludia:
        if clovek[1] <= den <= clovek[2]:
            if clovek[0] == 'M':
                muzov += 1
            elif clovek[0] == 'F':
                zien += 1
            else:
                print('WTF?!')

    parov = min(muzov, zien)
    maxi = max(maxi, parov)

print(maxi * 2)
