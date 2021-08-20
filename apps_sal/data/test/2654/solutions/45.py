N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    (A[i], B[i]) = map(int, input().split())
A.sort()
B.sort()
if N % 2 == 1:
    print(B[N // 2] - A[N // 2] + 1)
else:
    print(B[N // 2] + B[N // 2 - 1] - A[N // 2] - A[N // 2 - 1] + 1)
