r = int(input())
if r % 2 == 0 or r <= 4:
    print('NO')
else:
    y = (r - 3) // 2
    print(1, y)
