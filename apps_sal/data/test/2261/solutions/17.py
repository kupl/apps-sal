n = int(input())
k = 0
v = [[1]]
while(k < n):
    k = k + 1
    for i in range(len(v)):
        v[i].extend(v[i])
    for i in range(len(v)):
        v2 = []
        for j in range(len(v[i])):
            v2.append(v[i][j])
        v.append(v2)
    for i in range(int(len(v) / 2), len(v)):
        for j in range(int(len(v[i]) / 2), len(v[i])):
            v[i][j] = v[i][j] * (-1)
for i in range(len(v)):
    for j in range(len(v)):
        if(v[i][j] == 1):
            print('+', end="")
        else:
            print('*', end="")
    print()
