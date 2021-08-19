A = [[]] * 3
for row in range(3):
    A[row] = list(map(int, input().split()))
n = int(input())
B = [0] * n
for i in range(n):
    B[i] = int(input())
flag = False


def check_bingo(A, B):
    for row in range(3):
        if A[row][0] and A[row][1] and A[row][2]:
            return True
    for col in range(3):
        if A[0][col] and A[1][col] and A[2][col]:
            return True
    if A[0][0] and A[1][1] and A[2][2]:
        return True
    if A[0][2] and A[1][1] and A[2][0]:
        return True
    return False


for row in range(3):
    for col in range(3):
        if A[row][col] in B:
            A[row][col] = True
        else:
            A[row][col] = False
print('Yes' if check_bingo(A, B) else 'No')
