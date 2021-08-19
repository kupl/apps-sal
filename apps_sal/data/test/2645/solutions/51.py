S = input()
cp = 0
cg = 0
point = 0
for s in S:
    if s == 'g':
        if cp + 1 <= cg:
            point += 1
            cp += 1
        else:
            cg += 1
    elif cp + 1 <= cg:
        cp += 1
    else:
        point -= 1
        cg += 1
print(point)
