N = int(input())

s = input()
t = [["X"] * N for _ in range(4)]

if s[1] == "o":
    t[0][0], t[0][1], t[0][2] = "S", "S", "S"
    t[1][0], t[1][1], t[1][2] = "W", "S", "W"
    t[2][0], t[2][1], t[2][2] = "S", "W", "W"
    t[3][0], t[3][1], t[3][2] = "W", "W", "S"
else:
    t[0][0], t[0][1], t[0][2] = "S", "S", "W"
    t[1][0], t[1][1], t[1][2] = "W", "S", "S"
    t[2][0], t[2][1], t[2][2] = "S", "W", "S"
    t[3][0], t[3][1], t[3][2] = "W", "W", "W"

for i in range(4):
    for j in range(3, N):
        if (s[j - 1] == "o" and t[i][j - 1] == "S") or (s[j - 1] == "x" and t[i][j - 1] == "W"):
            t[i][j] = t[i][j - 2]
        else:
            if t[i][j - 2] == "S":
                t[i][j] = "W"
            else:
                t[i][j] = "S"
    flag = True
    if (s[0] == "o" and t[i][0] == "S") or (s[0] == "x" and t[i][0] == "W"):
        if t[i][-1] != t[i][1]:
            flag = False
    else:
        if t[i][-1] == t[i][1]:
            flag = False
    if (s[-1] == "o" and t[i][-1] == "S") or (s[-1] == "x" and t[i][-1] == "W"):
        if t[i][-2] != t[i][0]:
            flag = False
    else:
        if t[i][-2] == t[i][0]:
            flag = False
    if flag:
        print(*t[i], sep = "")
        return

print(-1)

