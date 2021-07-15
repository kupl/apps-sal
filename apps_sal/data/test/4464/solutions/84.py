a, b, c = map(int, input().split())

for i in range(b):
    if (a * i) % b == c:
        print('YES')
        break
    elif (a * i) % b == 0 and i > 0:
        print('NO')
        break
