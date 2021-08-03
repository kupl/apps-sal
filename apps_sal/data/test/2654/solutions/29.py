import statistics
N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
A.sort()
B.sort()
if N % 2 == 1:
    print(statistics.median(B) - statistics.median(A) + 1)
else:
    print(int(statistics.median(B) * 2 - statistics.median(A) * 2 + 1))
