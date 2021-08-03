# упрощенное вычисление C
def c2(n):
    return n * (n - 1) // 2


def c3(n):
    return n * (n - 1) * (n - 2) // 6


g, d, f = list(map(int, input().split()))
# Костыль
if g < 1 or d < 2 or f < 3:
    print(0)
    return

ans = 0
a = []
n = g + d + f
# скидываем все в один массив и запоминаем типы
for i in map(int, input().split()):
    a.append((i, 0))
for i in map(int, input().split()):
    a.append((i, 1))
for i in map(int, input().split()):
    a.append((i, 2))

# сортируем этот массив по номеру
a.sort()

for i in range(n):  # в i перебераем минимум
    types = [0, 0, 0]
    j = i + 0  # в j перебераем максимум
    while j < n and a[j][0] <= 2 * a[i][0]:  # если максимум в 2 раза меньше минимума, то и все остальные
        types[a[j][1]] += 1
        now_types = types.copy()
        now_types[a[j][1]] -= 1
        now_types[a[i][1]] -= 1
        # проверка на то, какого типа минимум и максимум, их мы не учитываем при подсчете кол-ва вариантов, потому что мы их зафиксировали, чтобы не было повторов
        if a[j][1] == 0 and a[i][1] == 1 or a[j][1] == 1 and a[i][1] == 0:
            if now_types[1] >= 1 and now_types[2] >= 3:
                ans += now_types[1] * c3(now_types[2])
        elif a[j][1] == 0 and a[i][1] == 2 or a[j][1] == 2 and a[i][1] == 0:
            if now_types[1] >= 2 and now_types[2] >= 2:
                ans += c2(now_types[1]) * c2(now_types[2])
        elif a[j][1] == 2 and a[i][1] == 1 or a[j][1] == 1 and a[i][1] == 2:
            if now_types[0] >= 1 and now_types[1] >= 1 and now_types[2] >= 2:
                ans += now_types[0] * now_types[1] * c2(now_types[2])
        elif a[j][1] == 1 and a[i][1] == 1:
            if now_types[0] >= 1 and now_types[2] >= 3:
                ans += now_types[0] * c3(now_types[2])
        elif a[j][1] == 2 and a[i][1] == 2:
            if now_types[0] >= 1 and now_types[1] >= 2 and now_types[2] >= 1:
                ans += now_types[0] * c2(now_types[1]) * now_types[2]
        j += 1
print(ans)
