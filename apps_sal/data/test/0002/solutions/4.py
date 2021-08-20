y = input()
ly = len(y)
iy = int(y)
td = iy / 10 ** (ly - 1)
if td == 9:
    print(10 ** ly - iy)
else:
    print((int(y[0]) + 1) * 10 ** (ly - 1) - iy)
