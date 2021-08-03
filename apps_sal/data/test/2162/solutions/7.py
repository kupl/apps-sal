import bisect
import sys
input = sys.stdin.readline

k1, k2, k3 = list(map(int, input().split()))

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

A = sorted(A1) + sorted(A2) + sorted(A3)


N = k1 + k2 + k3
DP = [float("inf")] * N

for a in A:
    pos = bisect.bisect_left(DP, a)
    DP[pos] = a

ANS = 0
for i in range(N):
    if DP[i] != float("inf"):
        ANS = i

print(N - (ANS + 1))
