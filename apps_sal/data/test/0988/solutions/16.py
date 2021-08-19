variants = []
price = ((3, 4, 3), (3, 4, 3), (2, 3, 2), (2, 3, 2), (1, 2, 1), (1, 2, 1))
max_price = (0, 0, 0, 0)
class_map = []
for i in range(6):
    current_row = input().split('-')
    class_map.append(current_row)
    for (j, parta) in enumerate(current_row):
        for (n, place) in enumerate(parta):
            if place == '.' and price[i][j] > max_price[0]:
                max_price = (price[i][j], i, j, n)
(i, j, n) = max_price[1:]
to_change = class_map[i][j]
if n:
    class_map[i][j] = class_map[i][j][0] + 'P'
else:
    class_map[i][j] = 'P' + class_map[i][j][1]
for row in class_map:
    print('-'.join(row))
