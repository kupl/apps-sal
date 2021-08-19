a, b = map(int, input().split())
print("40 100")

kuro = [["#" for i in range(100)] for j in range(20)]
siro = [["." for i in range(100)] for j in range(20)]

cou = 0
flag = False
for i in range(0, 20, 2):
    if flag:
        break
    for j in range(0, 100, 2):
        if cou >= a - 1:
            flag = True
            break
        elif cou < a - 1:
            cou += 1
            kuro[i][j] = "."

cou = 0
flag = False
for i in range(1, 20, 2):
    if flag:
        break
    for j in range(0, 100, 2):
        if cou >= b - 1:
            flag = True
            break
        elif cou < b - 1:
            cou += 1
            siro[i][j] = "#"

for i in range(20):
    for j in range(100):
        print(kuro[i][j], end="")
    print()
for i in range(20):
    for j in range(100):
        print(siro[i][j], end="")
    print()
