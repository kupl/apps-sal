w = 0
b = 0
for j in range(8):
    c = input()
    for i in range(8):
        if c[i] == 'Q':
            w += 9
        if c[i] == 'R':
            w += 5
        if c[i] == 'B' or c[i] == 'N':
            w += 3
        if c[i] == 'P':
            w += 1
        if c[i] == 'q':
            b += 9
        if c[i] == 'r':
            b += 5
        if c[i] == 'b' or c[i] == 'n':
            b += 3
        if c[i] == 'p':
            b += 1
if w > b:
    print('White')
elif b != w:
    print('Black')
else:
    print('Draw')
