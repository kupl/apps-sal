A = [0, 1, 2]
B = [0] * 6
for i in range(6):
    B[i] = A[:]
    if i % 2 == 0:
        A[0], A[1] = A[1], A[0]
    else:
        A[1], A[2] = A[2], A[1]
n = int(input())
#n -= 1
n %= 6
x = int(input())
print(B[n][x])
