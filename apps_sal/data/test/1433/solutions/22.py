(n, m) = map(int, input().split())
a = [''.join(input().split()) for i in range(n)]
columns = []
c = 0
for i in a:
    f = i.find('1')
    s = i.rfind('1')
    if f != -1 and s != -1:
        c += i[f:].count('0') + i[:s + 1].count('0')
for i in range(m):
    column = ''
    for j in range(n):
        column += a[j][i]
    columns.append(column)
for column in columns:
    f = column.find('1')
    s = column.rfind('1')
    if f != -1 and s != -1:
        c += column[f:].count('0') + column[:s + 1].count('0')
print(c)
