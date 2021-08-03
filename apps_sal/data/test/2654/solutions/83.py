N = int(input())
A = list()
B = list()
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if(N % 2 == 1):
    x = A[(N - 1) // 2]
    y = B[(N - 1) // 2]
    print(y - x + 1)
else:
    x = A[(N // 2) - 1] + A[N // 2]
    y = B[(N // 2) - 1] + B[N // 2]
    print(y - x + 1)
