import itertools
import bisect
n = int(input())
bo = list(map(int, input().split()))
cnt = 0
bo.sort()
for a in range(n - 1):
    for b in range(a + 1, n):
        cnt += bisect.bisect_left(bo, bo[a] + bo[b]) - (b + 1)
print(cnt)
