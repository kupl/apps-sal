N = int(input())
S = input()

A = [0] * N
B = [0] * N

for i in range(1, N):
    A[i] = A[i - 1] + (1 if S[i - 1] == 'W' else 0)
    B[N - i - 1] = B[N - i] + (1 if S[N - i] == 'E' else 0)

print(min(map(lambda x: x[0] + x[1], zip(A, B))))
