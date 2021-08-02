l = []
for i in range(4):
    l2 = input()
    l1 = []
    for j in range(4):
        l1.append(l2[j])
    l.append(l1)
r = 0
for i in range(3):
    for j in range(3):
        if(l[i][j] == l[i][j + 1]):
            if(l[i][j] == l[i + 1][j] or l[i][j] == l[i + 1][j + 1]):
                r = 1
                break
                break
for i in range(3):
    for j in range(4):
        if(l[i][j] == l[i + 1][j]):
            if((j != 3 and l[i][j] == l[i + 1][j + 1]) or (j != 0 and l[i][j] == l[i + 1][j - 1])):
                r = 1
                break
                break

if(r == 0):
    print("NO")
else:
    print("YES")
