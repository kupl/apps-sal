import sys
input = sys.stdin.readline


def print_ans(A):
    for a in A:
        print(" ".join(map(str, a)))


N = int(input())
if N <= 2:
    print(-1)
    return
if N == 3:
    A = [
        [1, 4, 9],
        [8, 3, 7],
        [2, 5, 6]
    ]
    print_ans(A)
    return
A = [
    [4, 3, 6, 12],
    [7, 5, 9, 15],
    [14, 1, 11, 10],
    [13, 8, 16, 2]
]
if N == 4:
    print_ans(A)
    return
A[0] += [1]
A[1] += [2]
A[2] += [3]
A[3] += [4]
A.append([8, 9, 6, 7, 5])
for y in range(4):
    for x in range(4):
        A[y][x] += 9
for y in range(5):
    for x in range(5):
        A[y][x] += N * N - 25
    A[y] += [-1] * (N - 5)
for y in range(5, N):
    A += [[-1] * N]
f = True
num = N * N - 25
for i in range(5, N):
    if f:
        for y in range(i):
            A[y][i] = num
            num -= 1
        for x in range(i, -1, -1):
            A[i][x] = num
            num -= 1
    else:
        for x in range(i):
            A[i][x] = num
            num -= 1
        for y in range(i, -1, -1):
            A[y][i] = num
            num -= 1
    f = not f
print_ans(A)
