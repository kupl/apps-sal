n, m = list(map(int,input().split()))
icon = [input() for i in range(n)]
faces = 0
for i in range(n-1):
    for j in range(m-1):
        temp = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        if icon[i][j] == "f":
            temp += 1
        elif icon[i][j] == "a":
            temp2 += 1
        elif icon[i][j] == "c":
            temp3 += 1
        elif icon[i][j] == "e":
            temp4 += 1
        if icon[i+1][j] == "f":
            temp += 1
        elif icon[i+1][j] == "a":
            temp2 += 1
        elif icon[i+1][j] == "c":
            temp3 += 1
        elif icon[i+1][j] == "e":
            temp4 += 1
        if icon[i][j+1] == "f":
            temp += 1
        elif icon[i][j+1] == "a":
            temp2 += 1
        elif icon[i][j+1] == "c":
            temp3 += 1
        elif icon[i][j+1] == "e":
            temp4 += 1
        if icon[i+1][j+1] == "f":
            temp += 1
        elif icon[i+1][j+1] == "a":
            temp2 += 1
        elif icon[i+1][j+1] == "c":
            temp3 += 1
        elif icon[i+1][j+1] == "e":
            temp4 += 1
        if temp == 1 and temp2 == 1 and temp3 == 1 and temp4 == 1:
            faces += 1
print(faces)

