s = str(input())
x1 = int(s[0])
x2 = int(s[1])
y = [[0] * 7 for i in range(10)]
y[0] = [1, 1, 1, 0, 1, 1, 1]
y[1] = [0, 0, 0, 0, 0, 1, 1]
y[2] = [0, 1, 1, 1, 1, 1, 0]
y[3] = [0, 0, 1, 1, 1, 1, 1]
y[4] = [1, 0, 0, 1, 0, 1, 1]
y[5] = [1, 0, 1, 1, 1, 0, 1]
y[6] = [1, 1, 1, 1, 1, 0, 1]
y[7] = [0, 0, 1, 0, 0, 1, 1]
y[8] = [1, 1, 1, 1, 1, 1, 1]
y[9] = [1, 0, 1, 1, 1, 1, 1]
q1 = 0
q2 = 0
sum = 0
flag = True
for i in range(100):
    q1 = i // 10
    q2 = i % 10
    for j in range(7):
        if int(y[x1][j]) - int(y[q1][j]) > 0:
            flag = False
        if int(y[x2][j]) - int(y[q2][j]) > 0:
            flag = False
    if flag:
        sum += 1
    flag = True
print(sum)
