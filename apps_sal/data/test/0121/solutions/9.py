fields = []
fields.append([input() for i in range(4)])
fields.append(['' for i in range(4)])
for i in range(4):
    c = 0
    for j in fields[0][i]:
        fields[1][c] += j
        c += 1
line1 = ''
line2 = ''
for i in range(4):
    line1 += fields[0][i][i]
    line2 += fields[0][i][3 - i]
fields.append([line1, line2])
fields[2].append(fields[0][1][0] + fields[0][2][1] + fields[0][3][2])
fields[2].append(fields[0][0][1] + fields[0][1][2] + fields[0][2][3])
fields[2].append(fields[0][0][2] + fields[0][1][1] + fields[0][2][0])
fields[2].append(fields[0][1][3] + fields[0][2][2] + fields[0][3][1])
for i in fields:
    for j in i:
        if 'x.x' in j or '.xx' in j or 'xx.' in j:
            print('YES')
            return
print('NO')
