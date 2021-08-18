h, w = map(int, input().split())
s = 0
li = []
lire = []
linew = []
for i in range(h):
    li.append(input())
for i in range(w):
    for j in range(h):
        if li[j][i] == ".":
            s = 1
        else:
            s = 0
            break
    if s == 1:
        lire.append(i)
        s = 0
for i in range(h):
    a = ""
    for j in range(w):
        if j not in lire:
            a += li[i][j]
    linew.append(a)
for i in range(len(linew)):
    if "
    continue
    else:
        print(linew[i])
