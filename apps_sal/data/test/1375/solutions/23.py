n = int(input())
mas = list(map(int, input().split(' ')))
mas2 = [0] * n
mas3 = [0] * n
summ = sum(mas)
if summ % 3 != 0:
    print(0)
else:
    summ /= 3
    su = 0
    schet = 0
    for i in range(n):
        su += mas[i]
        if su == summ:
            mas2[i] = 1
    su = 0
    schet = 0
    for i in range(n):
        su += mas[n - i - 1]
        if su == summ:
            schet += 1
        mas3[n - i - 1] = schet
    res = 0
    for i in range(n - 2):
        if mas2[i]:
            res += mas3[i + 2]
    print(res)
