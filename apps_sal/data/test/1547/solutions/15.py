n, m, k = map(int, input().split())
canvas = [['0']*m for i in range(n)]
comands = [input().split() for i in range(k)]
colored_rows = set()
colored_columns = set()
important_comands = []
while comands and len(colored_rows) != n and len(colored_columns) != m:
    comand = comands.pop()
    if comand[0] == '1':
        if comand[1] not in colored_rows:
            important_comands.append(comand)
            colored_rows.add(comand[1])
    else:
        if comand[1] not in colored_columns:
            important_comands.append(comand)
            colored_columns.add(comand[1])
for comand in important_comands[-1::-1]:
    mark, number, color = comand
    if mark == '1':
        canvas[int(number)-1] = [color]*m
    else:
        for i in range(n):
            canvas[i][int(number)-1] = color
for i in range(n):
    print(" ".join(canvas[i]))
