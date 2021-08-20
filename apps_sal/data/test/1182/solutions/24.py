def count(orchestra, initial, final):
    num = 0
    for i in range(initial[0], final[0] + 1):
        for j in range(initial[1], final[1] + 1):
            if orchestra[i][j] == 1:
                num += 1
    return num


def getNumber(orchestra, initial, minimum):
    num = 0
    for i in range(initial[0], r):
        for j in range(initial[1], c):
            final = [i, j]
            counter = count(orchestra, initial, final)
            if counter >= k:
                num += 1
    if initial[0] == len(orchestra):
        return num
    if initial[1] == len(orchestra[0]) - 1:
        initial[0] += 1
        initial[1] = 0
    else:
        initial[1] += 1
    return num + getNumber(orchestra, initial, minimum)


args = list(map(int, input().split()))
r = args[0]
c = args[1]
n = args[2]
k = args[3]
positions = []
for i in range(n):
    x = list(map(int, input().split()))
    positions.append([x[0], x[1]])
orchestra = [[0] * c for i in range(r)]
for i in positions:
    orchestra[i[0] - 1][i[1] - 1] = 1
print(getNumber(orchestra, [0, 0], k))
