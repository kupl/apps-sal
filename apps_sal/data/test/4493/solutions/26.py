c = [list(map(int, input().split())) for _ in range(3)]

a = [0, 0, 0]
b = [0, 0, 0]


def check(c, a, b):
    for i in range(3):
        for j in range(3):
            if a[i] + b[j] != c[i][j]:
                return False
    return True


for i in range(101):
    b[0] = i
    a[0] = c[0][0] - b[0]
    a[1] = c[1][0] - b[0]
    a[2] = c[2][0] - b[0]
    b[1] = c[0][1] - a[0]
    b[2] = c[0][2] - a[0]

    if check(c, a, b):
        print("Yes")
        return

print("No")
