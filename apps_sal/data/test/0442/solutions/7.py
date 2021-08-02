r = int(input())
if r <= 4 or r % 2 == 0:
    print('NO')
else:
    print(1, int((r - 3) / 2))
