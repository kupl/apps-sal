row, col = map(int, input().split(' '))
res = 0

if row > 1 and col > 1:
    res = (row - 2) * (col - 2)
elif row == 1 and col == 1:
    res = 1
elif row == 1:
    res = col - 2
else:
    res = row - 2

print(res)
