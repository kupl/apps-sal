(a, b) = map(int, input().split())
dis = a - b
if dis == 0:
    print('infinity')
else:
    res = 0
    x = 1
    while x ** 2 <= dis:
        if dis % x == 0 and x > b:
            res += 1
        if dis % x == 0 and dis // x > b and (x ** 2 != dis):
            res += 1
        x += 1
    print(res)
