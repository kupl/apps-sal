n, m, k = map(int, input().split())
row = (k + m * 2 - 1) // (m * 2)
table = (k - ((m * 2) * (row - 1) + 1)) // 2 + 1
place = ''
if k % 2 == 0:
    place = 'R'
else:
    place = 'L'
print(row, table, place)
