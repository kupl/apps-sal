n = int(input())
x = [int(i) for i in input().split()]
t = [0] * 3
k = 0
for i in range(n):
    for j in range(3):
        if x[i] == (j + 1):
            t[j] += 1
print(min(min(t[1], t[0]), t[2]))
i2 = 0
j = 0
z = [[0] * 3 for i in range(min(min(t[1], t[0]), t[2]))]
for j in range(3):
    while k < min(min(t[1], t[0]), t[2]):
        if x[i2] == (j + 1):
            z[k][j] = i2
            k += 1
        i2 += 1
    i2 = 0
    k = 0
for i in range(min(min(t[1], t[0]), t[2])):
    print(z[i][0] + 1, z[i][1] + 1, z[i][2] + 1)
