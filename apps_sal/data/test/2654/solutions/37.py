import statistics
N = int(input())
A = []
B = []
for i in range(N):
    (a, b) = list(map(int, input().split()))
    A.append(a)
    B.append(b)
Am = statistics.median(A)
Bm = statistics.median(B)
if N % 2 == 0:
    print(round(2 * (Bm - Am) + 1))
else:
    print(Bm - Am + 1)
