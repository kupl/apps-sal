import itertools
import sys
input = sys.stdin.readline
L = list(map(int, input().split()))
(A, B, C) = sorted(L)
ans = 0
if (B - A) % 2 == 0:
    ans += (B - A) // 2
    ans += C - B
else:
    ans += (B - A) // 2 + 1
    ans += 1
    ans += C - B
print(ans)
