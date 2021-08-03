import bisect as bi
n = int(input())
A = []
B = []
for i in range(n):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

A.sort()
B.sort()
if n % 2 == 1:
    a = A[(n - 1) // 2]
    b = B[(n - 1) // 2]

    print((b - a + 1))
else:
    a = (A[n // 2 - 1] + A[n // 2]) / 2
    b = (B[n // 2 - 1] + B[n // 2]) / 2

    print((int((b - a) / 0.5) + 1))
