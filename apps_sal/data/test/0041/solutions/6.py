from collections import deque
import sys

# def search(matrix, inicial, dirs, final):
#     queue = deque()
#     queue.append(inicial)
#     matrix[inicial[0]][inicial[1]] = 0
#     while len(queue) > 0:
#         aux = queue.popleft()
#
#         tupla = (aux[0], aux[1] + 1)
#         if matrix[tupla[0]][tupla[1]] != -1:
#             if matrix[tupla[0]][tupla[1]] == -9 or matrix[tupla[0]][tupla[1]] == -8:
#                 queue.append(tupla)
#                 matrix[tupla[0]][tupla[1]] = matrix[aux[0]][aux[1]]
#
#                 dirs[tupla[0]][tupla[1]] = 'R'
#                 if dirs[tupla[0]][tupla[1]] != dirs[aux[0]][aux[1]]:
#                     matrix[tupla[0]][tupla[1]] += 1
#
#         tupla = (aux[0], aux[1] - 1)
#         if matrix[tupla[0]][tupla[1]] != -1:
#             if matrix[tupla[0]][tupla[1]] == -9 or matrix[tupla[0]][tupla[1]] == -8:
#                 queue.append(tupla)
#                 matrix[tupla[0]][tupla[1]] = matrix[aux[0]][aux[1]]
#
#                 dirs[tupla[0]][tupla[1]] = 'L'
#                 if dirs[tupla[0]][tupla[1]] != dirs[aux[0]][aux[1]]:
#                     matrix[tupla[0]][tupla[1]] += 1
#
#         tupla = (aux[0] - 1, aux[1])
#         if matrix[tupla[0]][tupla[1]] != -1:
#             if matrix[tupla[0]][tupla[1]] == -9 or matrix[tupla[0]][tupla[1]] == -8:
#                 queue.append(tupla)
#                 matrix[tupla[0]][tupla[1]] = matrix[aux[0]][aux[1]]
#
#                 dirs[tupla[0]][tupla[1]] = 'U'
#                 if dirs[tupla[0]][tupla[1]] != dirs[aux[0]][aux[1]]:
#                     matrix[tupla[0]][tupla[1]] += 1
#
#
#         tupla = (aux[0] + 1, aux[1])
#         if matrix[tupla[0]][tupla[1]] != -1:
#             if matrix[tupla[0]][tupla[1]] == -9 or matrix[tupla[0]][tupla[1]] == -8:
#                 queue.append(tupla)
#                 matrix[tupla[0]][tupla[1]] = matrix[aux[0]][aux[1]]
#
#                 dirs[tupla[0]][tupla[1]] = 'D'
#                 if dirs[tupla[0]][tupla[1]] != dirs[aux[0]][aux[1]]:
#                     matrix[tupla[0]][tupla[1]] += 1
#
#
#
#
# n, m = map(int, sys.stdin.readline().strip().split(" "))
#
# matrix = []
# dirs = []
# aux = [-1 for i in range(m + 2)]
# matrix.append(aux)
# dirs.append(aux)
#
# inicial = ()
# final = ()
# for i in range(n):
#     line = [-1] + list(sys.stdin.readline().strip()) + [-1]
#     matrix.append(line)
#     aux = [-1 for i in range(m + 2)]
#     dirs.append(aux)
#     for j in range(1, m + 1):
#         if line[j] == 'S':
#             inicial = (i + 1, j)
#         elif line[j] == 'T':
#             matrix[i + 1][j] = -8
#             final = (i + 1, j)
#         elif line[j] == '*':
#             matrix[i + 1][j] = -10
#         elif line[j] == '.':
#             matrix[i + 1][j] = -9
#
# aux = [-1 for i in range(m + 2)]
# matrix.append(aux)
# dirs.append(aux)
#
# search(matrix, inicial, dirs, final)
# if matrix[final[0]][final[1]] <= 3 and matrix[final[0]][final[1]] >= 0:
#     print("YES")
# else:
#     print("NO")


n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split(" ")))
zeros = [-float('Inf')]
for i in range(n):
    if array[i] == 0:
        zeros.append(i)
zeros.append(float('Inf'))

j = 1
for i in range(n):
    if array[i] == 0:
        j += 1
        print(array[i], end=" ")
    else:
        aux = min(abs(zeros[j] - i), abs(zeros[j - 1] - i))
        print(aux, end=" ")
