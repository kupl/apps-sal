from statistics import median
N = int(input())
A = []
B = []
for i in range(0, N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A = sorted(A)
B = sorted(B)


if N % 2 == 1:
    print(median(B) - median(A) + 1)
else:
    print(int((median(B) - median(A)) * 2 + 1))
