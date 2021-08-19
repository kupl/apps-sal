import statistics
N = int(input())
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]
for k in range(N):
    (A[k], B[k]) = map(int, input().split())
if N % 2 == 1:
    print(statistics.median(B) - statistics.median(A) + 1)
else:
    print(int((statistics.median(B) - statistics.median(A)) * 2 + 1))
