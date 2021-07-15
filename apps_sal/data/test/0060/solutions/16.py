seat = input()
row, seat = int(seat[:-1]), seat[-1]
row -= 1
shift = {'f': 1, 'e': 2, 'd': 3, 'a': 4, 'b': 5, 'c': 6}
time = shift[seat]
if row % 4 == 2:
    row -= 1
elif row % 4 == 1:
    row += 1
row //= 2
time += 6 * row
time += row
time += 2 * (row // 2)
print(time)
