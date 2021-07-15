h, w = list(map(int, input().split()))
masu = []

for i in range(h):
    line = list(input())
    if line != ["."] * w:
        masu.append(line)

h = len(masu)
del_i = []
for i in range(w):
    for j in range(h):
        if masu[j][i] != ".":
            break
    else:
        del_i.append(i)
w = len(del_i)
for j in range(w):
    for i in range(h):
        masu[i].pop(del_i[j] - j)

for i in range(h):
    print(("".join(masu[i])))

