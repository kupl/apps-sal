N = int(input())
first = []
second = []
for i in range(N):
    first.append([s for s in input()])
for i in range(N):
    second.append([s for s in input()])


def rotate_90(matrix):
    return list(zip(*matrix[::-1]))


def flip(matrix):
    return matrix[::-1]


def compare_matrices(first, second):
    for i in range(N):
        for j in range(N):
            if first[i][j] != second[i][j]:
                return False
    return True


def wrap(first, second):
    if compare_matrices(first, second) == True:
        return 'Yes'
    hold_first = first[::]
    for _ in range(3):
        first = rotate_90(first)
        if compare_matrices(first, second) == True:
            return 'Yes'
    first = hold_first
    first = flip(first)
    if compare_matrices(first, second) == True:
        return 'Yes'
    for _ in range(3):
        first = rotate_90(first)
        if compare_matrices(first, second) == True:
            return 'Yes'
    return 'No'


print(wrap(first, second))
