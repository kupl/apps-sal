def printrow(num, s, t):
    for i in range(50):
        res = []
        for j in range(100):
            if (i + j) % 3 == 0 and (num - 1) * i > 0:
                res.append(s)
                num -= 1
            else:
                res.append(t)
        print(*res, sep='')


a, b = map(int, input().split())

print(100, 100)
printrow(b, '
printrow(a, '.', '
