(x, y, z) = list(map(int, input().split()))
c = x // z + y // z
rx = x % z
ry = y % z
if rx + ry < z:
    print(f'{c} 0')
elif rx > ry:
    print(f'{c + 1} {z - rx}')
else:
    print(f'{c + 1} {z - ry}')
