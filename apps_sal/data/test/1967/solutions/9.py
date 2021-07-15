w, h = map(int, input().split())
listGorizontal = []
listVertical = []
for i in range(h):
    listGorizontal.append(input())
for i in range(h):
    s = ""
    k = w
    for j in listGorizontal[i]:
        s += j[w - k]*2
    listVertical.append(s)
s = ""
k = h
for i in range(2*w):
    for j in range(h):
        s += 2 * listVertical[h - k][i]
        k += -1
    k = h
    if i != 2*w :
        s += "\n"
print(s)
