h, w = list(map(int, input().split()))
a = []
for i in range(h):
    line = input()
    if line != "." * w:
        a.append(list(line))

h = len(a)

w_pass = []
for i in range(w):
    for j in range(h):
        if a[j][i] != ".":
            break
    else:
        w_pass.append(i)

for i in range(h):
    line = ""
    for j in range(w):
        if j in w_pass:
            pass
        else:
            line += a[i][j]
    print(line)
