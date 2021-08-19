N = int(input())
A = [0] * N
B = list(map(int, input().split()))
A[0] = B[0]
A[-1] = B[-1]
for n in range(1, N - 1):
    A[n] = min(B[n - 1], B[n])
print(sum(A))
