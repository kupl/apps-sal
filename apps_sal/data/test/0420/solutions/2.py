def can_mirror(matrix):
    if len(matrix) % 2 != 0:
        return False
    mid = len(matrix) // 2
    for i in range(mid):
        lower = -i-1
        if matrix[mid+lower] != matrix[mid+i]:
            return False
    return True


def mirror(matrx):
    mid = len(matrix) // 2
    return matrix[:mid]


n, m = list(map(int, input().split()))
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
while can_mirror(matrix):
    matrix = mirror(matrix)
print(len(matrix))

