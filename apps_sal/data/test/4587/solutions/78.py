import bisect
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
C = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
C.sort()

ans = 0
for b in B:
    cnt1 = bisect.bisect_left(A, b)
    cnt2 = len(C) - bisect.bisect(C, b)

    ans += cnt1 * cnt2

print(ans)
