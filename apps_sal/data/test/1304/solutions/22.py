lines = []
for i in range(11):
    lines.append(input())
coords = list(map(int, input().split()))
sqy = (coords[0] - 1) % 3
sqx = (coords[1] - 1) % 3
startchange = False
sqstart = {0: 0, 1: 4, 2: 8}
changesyms = {'x': 'x', 'o': 'o', '.': '!', ' ': ' ', '\n': '\n'}
free = 0
toprint = ''
toprint2 = ''
for i in range(11):
    for i1 in range(len(lines[i])):
        if i in range(sqstart[sqy], sqstart[sqy] + 3) and i1 in range(sqstart[sqx], sqstart[sqx] + 3):
            startchange = True
        else:
            startchange = False
        if startchange:
            toprint += changesyms[lines[i][i1]]
            if changesyms[lines[i][i1]] != lines[i][i1]:
                free += 1
        else:
            toprint += lines[i][i1]
if free == 0:
    startchange = True
else:
    startchange = False
syms = 0
for i in toprint:
    if startchange:
        toprint2 += changesyms[i]
        if i not in changesyms:
            toprint2 += i
    else:
        toprint2 += i
    syms += 1
    if syms % 11 == 0 and syms != 99:
        toprint2 += '\n'
    if syms % 33 == 0 and syms != 99:
        toprint2 += '\n'
print(toprint2)
