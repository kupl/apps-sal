from sys import stdin
firstline = stdin.readline().rstrip().split()
rows = int(firstline[0])
cols = int(firstline[1])
k = int(firstline[2])

flip = True
flat_matrix=[]
for row in range(rows):
    col_traversal = (range(cols-1, -1, -1), range(cols))[flip]
    for col in col_traversal:
        flat_matrix.append((row+1, col+1))
    flip = not flip

point = 0
for tube in range(k):
    if tube != k-1:
        print("2 ", end='')
        for cell in range(2):
            point + cell
            print(str(flat_matrix[point+cell][0]) + " " + str(flat_matrix[point+cell][1]) + " ", end='')
        point += 2
        print()
    else:
        print(str(len(flat_matrix)-point) + " ", end='')
        for cell in range(len(flat_matrix)-point):
            print(str(flat_matrix[point+cell][0]) + " " + str(flat_matrix[point+cell][1]) + " ", end='')
print()

