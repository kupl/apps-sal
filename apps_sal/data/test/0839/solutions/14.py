def fun(mas, h):
    nonlocal ans, a

    if (h < 5):
        for i in range(5):
            if not(i in mas):
                fun(mas + [i], h + 1)
        return 0

    res = 0
    for i in range(5):
        if (len(mas) > 1):
            res += a[mas[0]][mas[1]]
            res += a[mas[1]][mas[0]]
        if (len(mas) > 3):
            res += a[mas[2]][mas[3]]
            res += a[mas[3]][mas[2]]
        mas.pop(0)

    if (res > ans):
        ans = res


a = [[0] * 5] * 5

for i in range(5):
    a[i] = [int(j) for j in input().split()]

ans = 0
for i in range(5):
    mas = [i]
    fun(mas, 1)

print(ans)
