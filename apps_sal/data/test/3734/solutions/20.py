d = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
first = d[input()]
second = d[input()]
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for i in range(11):
    (m1, m2) = (months[i], months[i + 1])
    if (m1 + first) % 7 == second:
        print('YES')
        break
else:
    print('NO')
