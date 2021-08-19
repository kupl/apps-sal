import sys
import bisect

input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        l = L[i] + L[j]
        p = bisect.bisect_left(L, l)
        # print(p)
        ans += p - j - 1

print(ans)
