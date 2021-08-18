def is_valid(m, a, b):
    for i in range(3):
        for j in range(3):
            if (m[i][j] != a[i] + b[j]):
                return 0
    return 1


m = []
for a0 in range(3):
    m.append(list(map(int, input().split())))

for a0 in range(101):
    b0 = m[0][0] - a0
    b1 = m[0][1] - a0
    b2 = m[0][2] - a0
    a1 = m[1][0] - b0
    a2 = m[2][0] - b0
    if (is_valid(m, [a0, a1, a2], [b0, b1, b2])):
        print("Yes")
        return
print("No")
