import sys

n, m = list(map(int, input().split()))


def read_matrix():
    M = []
    for i in range(n):
        M.append(list(map(int, input().split())))
    return M


A, B = read_matrix(), read_matrix()


for i in range(n):
    for j in range(m):
        A[i][j], B[i][j] = min(A[i][j], B[i][j]), max(A[i][j], B[i][j])
        if i > 0 and (A[i][j] <= A[i - 1][j] or B[i][j] <= B[i - 1][j]) or \
                j > 0 and (A[i][j] <= A[i][j - 1] or B[i][j] <= B[i][j - 1]):
            print('Impossible')
            return

print('Possible')
