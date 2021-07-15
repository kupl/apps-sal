msg_in = input().split()
x = int(msg_in[0])
y = int(msg_in[1])
num_of_transform = [0, 0]
matrix = []
blank = []
for i in range(y+2):
    blank.append(' ')
matrix.append(blank)
for i in range(x):
    msg_in = input()
    matrix.append([' '])    
    for j in msg_in:
        matrix[i+1].append(j)
    matrix[i+1].append(' ')
matrix.append(blank)
while True:
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            sum = 0
            if matrix[i][j] != ' ':
                if matrix[i][j-1] == matrix[i][j]:
                    sum += 1
                if matrix[i][j+1] == matrix[i][j]:
                    sum += 1
                if matrix[i-1][j] == matrix[i][j]:
                    sum += 1
                if matrix[i+1][j] == matrix[i][j]:
                    sum += 1
                if sum < 2:
                    matrix[i][j] = ' '
                    num_of_transform[0] += 1
    if num_of_transform[0] == x * y:
        print('No')
        break
    elif num_of_transform[0] == num_of_transform[1]:
        print('Yes')
        break
    else:
        num_of_transform[1] = num_of_transform[0]

