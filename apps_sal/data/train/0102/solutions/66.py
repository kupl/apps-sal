n = int(input())
for i in range(n):
    x = input()
    col = (len(x) - 1) * 9
    la = int(x)
    s = ''
    for i in range(len(x)):
        s += '1'
    for i in range(9):
        if (int(s) * (i + 1) <= la):
            col += 1
    print(col)
