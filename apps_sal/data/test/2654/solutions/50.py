N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N % 2 == 0:
    n = N // 2
    print(B[n] + B[n - 1] - A[n] - A[n - 1] + 1)
else:
    n = N // 2
    print((B[n] - A[n] + 1))
