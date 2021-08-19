N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0] * N
C[0] = A[0] + sum(B)
for i in range(1, N):
    C[i] = C[i - 1] + A[i] - B[i - 1]
print(max(C))
