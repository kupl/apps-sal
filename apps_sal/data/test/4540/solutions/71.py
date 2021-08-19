N = int(input())
A = [0] + list(map(int, input().split())) + [0]
B = [abs(a - b) for (a, b) in zip(A, A[1:])]
C = sum(B)
for n in range(N):
    print(C + abs(A[n] - A[n + 2]) - (B[n] + B[n + 1]))
