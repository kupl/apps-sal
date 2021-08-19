(a, b, c) = map(int, input().split())
i = 0
flag = True
while flag:
    num = b * i
    if (num + c) % a == 0:
        print('YES')
        flag = False
    elif i >= 10 ** 5:
        print('NO')
        break
    else:
        i += 1
