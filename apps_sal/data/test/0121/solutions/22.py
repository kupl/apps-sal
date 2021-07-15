def check(a):
    for i in range(4):
        if "xxx" in a[i]:
            return True
    if a[1][0] == "x" and a[2][0] == "x" and (a[0][0] == "x" or a[3][0] == "x"):
        return True
    if a[1][1] == "x" and a[2][1] == "x" and (a[0][1] == "x" or a[3][1] == "x"):
        return True
    if a[1][2] == "x" and a[2][2] == "x" and (a[0][2] == "x" or a[3][2] == "x"):
        return True
    if a[1][3] == "x" and a[2][3] == "x" and (a[0][3] == "x" or a[3][3] == "x"):
        return True
    if a[0][2] == a[1][1] == a[2][0] == "x":
        return True
    if a[1][2] == a[2][1] == "x" and (a[3][0] == "x" or a[0][3] == "x"):
        return True
    if a[3][1] == a[2][2] == a[1][3] == "x":
        return True
    if a[0][1] == a[1][2] == a[2][3] == "x":
        return True
    if a[1][0] == a[2][1] == a[3][2] == "x":
        return True
    if a[1][1] == a[2][2] == "x" and (a[0][0] == "x" or a[3][3] == "x"):
        return True
    return False



a, flag = [input() for i in range(4)], False
for i in range(4):
    for j in range(4):
        if a[i][j] == ".":
            b = a[:]
            str = b[i]
            b[i] = str[:j] + "x" + str[j + 1:]
            if check(b):
                flag = True
if flag:
    print("YES")
else:
    print("NO")
