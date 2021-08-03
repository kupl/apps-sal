h, w = map(int, input().split())
a = [input() for _ in range(h)]

hl = []
wl = []

for i in range(h):
    if a[i] == "." * w:
        hl += [i]
for i in range(w):
    if all([a[j][i] == "." for j in range(h)]):
        wl += [i]


for i in range(h):
    if i not in hl:
        for j in range(w):
            if j not in wl:
                print(a[i][j], end="")
        else:
            print("")
