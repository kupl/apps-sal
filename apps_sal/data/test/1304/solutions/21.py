def prnt(p):
    for i in p:
        for i3 in range(3):
            for i2 in i:
                for i4 in i2[i3]:
                    print(i4, end="")
                print(" ", end="")
            print()
        print()


p = []
for y1 in range(3):
    p.append([[], [], []])
    for y2 in range(3):
        s = input()
        if not s:
            s = input()
        s = s.split()
        for i in range(3):
            p[y1][i].append(list(s[i]))

crds = list(map(int, input().split()))
crds[0] -= 1
crds[1] -= 1

x1 = crds[0] // 3
y1 = crds[1] // 3
y2 = crds[0] % 3
x2 = crds[1] % 3

have_space = False
for i in p[y2][x2]:
    for i2 in i:
        if i2 == ".":
            have_space = True
            break

if have_space:
    for i in range(len(p[y2][x2])):
        for i2 in range(len(p[y2][x2][i])):
            if p[y2][x2][i][i2] == ".":
                p[y2][x2][i][i2] = "!"
else:
    for i1 in range(3):
        for i2 in range(3):
            for i3 in range(3):
                for i4 in range(3):
                    if p[i1][i2][i3][i4] == ".":
                        p[i1][i2][i3][i4] = "!"

prnt(p)
