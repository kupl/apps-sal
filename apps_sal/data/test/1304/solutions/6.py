field = [[0] for i in range(11)]
for i in range(11):
    field[i] = input().replace(" ", "")
save = field
field = []
for i in range(11):
    if(save[i] != ""):
        field.append([])
        for j in range(9):
            field[len(field) - 1].append(save[i][j])
x, y = map(int, input().split())
x, y = x - 1, y - 1
x1 = x % 3 * 3 + 1
y1 = y % 3 * 3 + 1
mark = False
for i in range(-1, 2):
    for j in range(-1, 2):
        if(field[x1 + i][y1 + j] == "."):
            mark = True
            field[x1 + i][y1 + j] = "!"
if not mark:
    for i in range(9):
        for j in range(9):
            if(field[i][j] == "."):
                field[i][j] = "!"
                
for i in range(9):
    for j in range(9):
        print(field[i][j], end="")
        if((j + 1) % 3 == 0):
            print(end=" ")
    if((i + 1) % 3 == 0):
        print()
    print()
    


