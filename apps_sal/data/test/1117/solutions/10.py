n = int(input())
mas = []
for i in range(n):
    mas.append(list(map(int, input().split())))
cur = 10 ** 9 + 1
for i in range(n):
    if cur < min(mas[i]):
        print('NO')
        break
    elif cur < max(mas[i]):
        cur = min(mas[i])
    else:
        cur = max(mas[i])
else:
    print('YES')
