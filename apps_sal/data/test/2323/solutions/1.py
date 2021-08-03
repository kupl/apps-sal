from bisect import bisect_left as bl
import sys
input = sys.stdin.readline
N = int(input())
A = sorted([int(a) for a in input().split()])
Q = int(input())

B = sorted([A[i + 1] - A[i] for i in range(N - 1)])
C = [0] * N
for i in range(1, N):
    C[i] = C[i - 1] + B[i - 1]
ANS = []
for q in range(Q):
    l, r = list(map(int, input().split()))
    k = r - l + 1
    i = bl(B, k)
    ANS.append(k * (N - i) + C[i])

print(*ANS)
