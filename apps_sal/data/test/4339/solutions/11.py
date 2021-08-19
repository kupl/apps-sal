from bisect import bisect_right
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [a - b for (a, b) in zip(A, B)]
C.sort()
ans = 0
for (i, c) in enumerate(C):
    ind = bisect_right(C, -c)
    ans += min(N - ind, N - i - 1)
print(ans)
