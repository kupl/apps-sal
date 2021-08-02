N = int(input())
A = list(map(int, input().split()))

temp = sum(A)
for i in range(1, N, 2):
    temp -= A[i] * 2

R = [0] * N
R[0] = temp

for i in range(1, len(R)):
    R[i] = A[i - 1] * 2 - R[i - 1]

print(*R)
