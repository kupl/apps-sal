from bisect import bisect_right
from itertools import accumulate


N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))

B_to_C = [0] * (N + 1)
for i in range(N):
    idx = bisect_right(C, B[i])
    B_to_C[i + 1] = N - idx
B_to_C = list(accumulate(B_to_C))

ans = 0
for i in range(N):
    idx = bisect_right(B, A[i])
    ans += B_to_C[N] - B_to_C[idx]
print(ans)
