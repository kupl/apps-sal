import bisect
import itertools
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
b_counts = [0] * N
for i in range(N):
    b_count = bisect.bisect_left(A, B[i])
    b_counts[i] = b_count
cumsum_b_counts = list(itertools.accumulate(b_counts))
cumsum_b_counts = [0] + cumsum_b_counts
total = 0
for c in C:
    count = bisect.bisect_left(B, c)
    total += cumsum_b_counts[count]
print(total)
