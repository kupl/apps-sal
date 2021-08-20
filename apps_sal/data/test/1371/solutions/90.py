S = int(input())
A = [0, 0, 0, 1, 1, 1, 2, 3, 4, 6] + [0] * S
for i in range(5, len(A)):
    A[i] = (A[i - 1] + A[i - 3]) % (10 ** 9 + 7)
print(A[S])
