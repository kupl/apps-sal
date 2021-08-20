import bisect
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [A[i] - B[i] for i in range(n)]
C.sort()
ANS = 0
for i in range(n):
    x = bisect.bisect_right(C, -C[i])
    ANS += n - max(x, i + 1)
print(ANS)
