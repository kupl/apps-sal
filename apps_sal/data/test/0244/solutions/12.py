def read(type=int):
    return type(input())


def read_arr(type=int):
    return [type(token) for token in input().split()]


n = read()
x = read()
n %= 6
A = [[0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1], [0, 2, 1]]
print(A[n][x])
