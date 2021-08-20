n = int(input())
x = list(map(int, input().strip().split(' ')))
x.sort()
try:
    znak = True
    for i in range(len(x)):
        for j in range(i + 1, len(x) - 1):
            if x[i] + x[j] > x[j + 1]:
                print('YES')
                znak = False
                1 / 0
    if znak:
        print('NO')
except:
    pass
