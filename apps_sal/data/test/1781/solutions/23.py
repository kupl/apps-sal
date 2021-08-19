n, k = list(map(int, input().split()))
rows = list()
# здесь и далее nb - neighbors
nb = 0
# места с соответствующим количеством соедей (0,1,2)
places_by_nb = [list(), list(), list()]
for i in range(n):
    # считываем строку и добавляем как массив
    line = input()
    rows.append(list(line))
    # вставляем символы-ограничители в начало и конец и идем по строке
    row = '-%s-' % line
    for j in range(1, 13):
        # вычисляем первоначальное количество соседей
        if row[j] == 'S':
            if row[j - 1] == 'S' or row[j - 1] == 'P':
                nb += 1
            if row[j + 1] == 'S' or row[j + 1] == 'P':
                nb += 1
        # вычисляем количество соседей у каждого свободного места
        # и записываем координату места (с учетом ограничителей) в соответствующий массив (по числу соседей)
        elif row[j] == '.':
            t = 0
            if row[j - 1] == 'S':
                t += 1
            if row[j + 1] == 'S':
                t += 1
            places_by_nb[t].append((i, j - 1))
# до тех пор пока есть непосаженные пассажиры:
# берем место, садим пассажира, увеличиваем количество соседей, уменьшаем количество пассажиров
for m in range(0, 3):
    while k > 0 and len(places_by_nb[m]) > 0:
        place = places_by_nb[m].pop(-1)
        rows[place[0]][place[1]] = 'x'
        nb += m
        k -= 1
    if k == 0:
        break
# и наконец выводим результат
print(nb)
for row in rows:
    print(''.join(row))
