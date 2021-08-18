b = False
s = []
for i in range(0, 4):
    st = str(input())
    s.append(st)
for i in range(0, len(s) - 1):
    for j in range(0, len(s[i]) - 1):
        x = 0
        if s[i][j] == '
        x += 1
        if s[i + 1][j] == '
        x += 1
        if s[i][j + 1] == '
        x += 1
        if s[i + 1][j + 1] == '
        x += 1
        if x != 2:
            print("YES")
            b = True
            break
    if b == True:
        break
if b == False:
    print("NO")
