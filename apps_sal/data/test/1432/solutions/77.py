N = int(input())
*A, = map(int, input().split())
B = [0] * N
a1 = A[0]
i = 1
while i < N:
    a1 += A[i + 1] - A[i]
    i += 2
B[0] = a1
i = 1
while i < N:
    B[i] = 2 * (A[i - 1] - B[i - 1] // 2)
    i += 1
print(*B)
