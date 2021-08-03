def II(): return int(input())


n = II()
for i in range(n):
    if 360 % (180 - II()):
        print('NO')
    else:
        print('YES')
