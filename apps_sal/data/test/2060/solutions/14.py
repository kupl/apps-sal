n = int(input())
for i in range(n):
    x = int(input())
    for a in range(x // 3 + 1):
        if (x - a * 3) % 7 == 0:
            print('YES')
            break
    else:
        print('NO')

