n, a, b = list(map(int, input().split()))
mas = [[0, 0] for i in range(n)]
for i in range(n):
    mas[i] = list(map(int, input().split()))


def f(i1, j1, i2, j2):
    if (i1 <= a and j1 <= b and i2 <= a and j2 <= b):
        if (j1 + j2 > b and i1 + i2 > a):
            return 0
        return i1 * j1 + i2 * j2
    return 0


ans = 0
for i in range(n):
    for j in range(n):
        if (i != j):
            ans = max(ans, f(mas[i][0], mas[i][1], mas[j][0], mas[j][1]))
            ans = max(ans, f(mas[i][1], mas[i][0], mas[j][0], mas[j][1]))
            ans = max(ans, f(mas[i][0], mas[i][1], mas[j][1], mas[j][0]))
            ans = max(ans, f(mas[i][1], mas[i][0], mas[j][1], mas[j][0]))

print(ans)
