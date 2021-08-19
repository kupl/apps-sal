desc = []
for i in range(8):
    input_str = input()
    desc.append(input_str)
w, b = 0, 0
""" вес ферзя равен 9,
вес ладьи равен 5,
вес слона равен 3,
вес коня равен 3,
вес пешки равен 1, """
for i in range(8):
    for j in range(8):
        if desc[i][j] == 'Q':
            w += 9
        elif desc[i][j] == 'q':
            b += 9
        elif desc[i][j] == 'R':
            w += 5
        elif desc[i][j] == 'r':
            b += 5
        elif desc[i][j] == 'B':
            w += 3
        elif desc[i][j] == 'b':
            b += 3
        elif desc[i][j] == 'N':
            w += 3
        elif desc[i][j] == 'n':
            b += 3
        elif desc[i][j] == 'P':
            w += 1
        elif desc[i][j] == 'p':
            b += 1
        else:
            pass
if w > b:
    print("White")
elif b > w:
    print("Black")
else:
    print("Draw")
# ферзь обозначается символом 'Q', ладья — 'R', слон — 'B', конь — 'N', пешка — 'P', король — 'K'.
