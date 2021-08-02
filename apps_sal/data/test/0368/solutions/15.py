import sys
w = 0
b = 0
for i in range(8):
    n = list(sys.stdin.readline())
    for j in n:
        if j == 'q':
            w = w + 9
        if j == 'Q':
            b = b + 9
        if j == 'r':
            w = w + 5
        if j == 'R':
            b = b + 5
        if j == 'b':
            w = w + 3
        if j == 'B':
            b = b + 3
        if j == 'n':
            w = w + 3
        if j == 'N':
            b = b + 3
        if j == 'p':
            w = w + 1
        if j == 'P':
            b = b + 1
if w < b: print("White")
elif w > b: print("Black")
else: print("Draw")
