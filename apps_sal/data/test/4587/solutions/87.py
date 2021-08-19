import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = sorted(A)
B = sorted(B)
C = sorted(C)
Count_A = [0] * N
Count_C = [0] * N
for i in range(N):
    Count_A[i] = bisect.bisect_left(A, B[i])
    Count_C[i] = N - bisect.bisect(C, B[i])
Patterns = 0
for i in range(N):
    Patterns = Patterns + Count_A[i] * Count_C[i]
print(Patterns)
