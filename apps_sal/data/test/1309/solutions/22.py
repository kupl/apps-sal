n = int(input())
w = list(map(int, input().split()))

w.sort()

d = []

# Решаем перебором, выбрасываем из списка 2 каякеров и
# находим сумму разностей весов у оставшихся, отсортированных по возрастанию
for i in range(0, 2 * n):
    for j in range(i + 1, 2 * n):
        if i == j:
            continue

        tw = list(w)
        tw.pop(i)
        tw.pop(j - 1)

        td = 0
        for k in range(0, len(tw), 2):
            td += tw[k + 1] - tw[k]

        d.append(td)

print(min(d))
