num_line = input().split(" ")
x_num = int(num_line[0])
y_num = int(num_line[1])
num = int(num_line[2])

tangle = [[1] * x_num for i in range(y_num)]

# print(tangle)

for i in range(num):
    line = input().split(" ")
    x_tem = int(line[0])
    y_tem = int(line[1])
    index = int(line[2])

    if(index == 1):
        for j in range(y_num):
            for k in range(x_tem):
                tangle[j][k] = 0
        # print(tangle)

    elif(index == 2):
        for j in range(y_num):
            for k in range(x_num - x_tem):
                tangle[j][k + x_tem] = 0
        # print(tangle)

    elif(index == 3):
        for j in range(y_tem):
            for k in range(x_num):
                tangle[j][k] = 0
        # print(tangle)

    else:
        for j in range(y_num - y_tem):
            for k in range(x_num):
                tangle[j + y_tem][k] = 0
        # print(tangle)

result = 0
for i in range(y_num):
    for j in range(x_num):
        result += tangle[i][j]

print(result)
