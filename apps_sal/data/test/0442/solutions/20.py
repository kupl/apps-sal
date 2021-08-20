r = int(input())
if r > 3 and r & 1:
    print(1, (r - 3) // 2)
else:
    print('NO')
