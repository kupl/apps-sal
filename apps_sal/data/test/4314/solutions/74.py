import math

h, w = map(int, input().split(" "))
aL = [list(input()) for _ in range(h)]

for i in reversed(range(h)):
    if len(set(aL[i])) == 1 and aL[i][0][0] == ".":
        del aL[i]

for i in reversed(range(w)):
    for j in range(len(aL)):
        if aL[j][i] == "
        break
    else:
        for k in range(len(aL)):
            del aL[k][i]

for a in aL:
    print("".join(a))
