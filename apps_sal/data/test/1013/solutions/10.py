tableData = input().split(' ')
rows = int(tableData[0])
cols = int(tableData[1])
table = []
for r in range(rows):
    table.append(input().split(' '))
found = False
for i in range(rows):
    if table[i][0] == '1' or table[i][cols - 1] == '1':
        found = True
        break
if not found:
    for i in range(cols):
        if table[0][i] == '1' or table[rows - 1][i] == '1':
            found = True
            break
if found:
    print('2')
else:
    print('4')
