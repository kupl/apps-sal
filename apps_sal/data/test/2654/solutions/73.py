import statistics
N = int(input())
A = []
B = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 1:
    med_min = A[N // 2]
    med_max = B[N // 2]
    print((med_max - med_min + 1))
else:
    med_min_db = A[N // 2] + A[N // 2 - 1]
    med_max_db = B[N // 2] + B[N // 2 - 1]
    print((med_max_db - med_min_db + 1))
