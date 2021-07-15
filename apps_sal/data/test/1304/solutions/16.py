def inp():
    b = []
    for i in range(3):
        for j in range(3):
            s = input()
            s = s[:3] + s[4:7] + s[8:]
            b.append(list(s))
        if i!=2:
            input()
    return b
def out():
    for i in range(3):
        for j in range(3):
            s = a[i * 3 + j]
            print(s[0],s[1],s[2],' ', s[3],s[4],s[5],' ', s[6],s[7],s[8], sep = '')
        if i!=2:
            print()


a = inp()
x, y = map(int,input().split())
x -= 1
y -= 1
x %= 3
y %= 3
f = True
for i in range(3):
    for j in range(3):
        if a[x * 3 + i][y * 3 + j] == '.':
            a[x * 3 + i][y * 3 + j] = '!'
            f = False
if f:
    for i in range(9):
        for j in range(9):
            if a[i][j] == '.':
                 a[i][j] = '!'
out()
            

