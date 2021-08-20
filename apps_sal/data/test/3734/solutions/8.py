a = input()
b = input()
D = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
(x, y) = (D[a], D[b])
if (y - x) % 7 == 2 or (y - x) % 7 == 3 or (y - x) % 7 == 0:
    print('YES')
else:
    print('NO')
