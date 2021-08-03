N = int(input())
B = list(map(int, input().split()))
A = [0] * (N)
A[0] = B[0]

for i in range(N - 1):
    A[i + 1] = B[i]
    if A[i] > B[i]:
        A[i] = B[i]

print(sum(A))
