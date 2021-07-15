matrix = []
matrix.append(''.join(input().split()))
matrix.append(''.join(input().split()))
matrix.append(''.join(input().split()))
input()
matrix.append(''.join(input().split()))
matrix.append(''.join(input().split()))
matrix.append(''.join(input().split()))
input()
matrix.append(''.join(input().split()))
matrix.append(''.join(input().split()))
matrix.append(''.join(input().split()))
x, y = list(map(int, input().split()))
x -= 1
y -= 1
flag = True
for i in range(x % 3 * 3, x % 3 * 3 + 3):
    for j in range(y % 3 * 3, y % 3 * 3 + 3):
        if matrix[i][j] == '.':
            flag = False
            matrix[i] = matrix[i][:j] + '!' + matrix[i][j + 1:]
if flag:
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == '.':
                matrix[i] = matrix[i][:j] + '!' + matrix[i][j + 1:]
for i in range(3):
    print(matrix[i][:3], matrix[i][3:6], matrix[i][6:9])
print()
for i in range(3, 6):
    print(matrix[i][:3], matrix[i][3:6], matrix[i][6:9])
print()
for i in range(6, 9):
    print(matrix[i][:3], matrix[i][3:6], matrix[i][6:9])

