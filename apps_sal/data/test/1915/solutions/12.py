n = int(input())
trian_Pask = [[0] * n for i in range(n)]


def strspace(k):
    spaces = 6 - len(str(k))
    return ' ' * spaces + str(k)


for y in range(n):
    for x in range(n):
        if x == 0 or y == 0:
            trian_Pask[y][x] = 1
        else:
            trian_Pask[y][x] = trian_Pask[y - 1][x] + trian_Pask[y][x - 1]

print(trian_Pask[n - 1][n - 1])
