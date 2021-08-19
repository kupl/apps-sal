import collections
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
c = collections.Counter(a)
cnt = 0
for (i, v) in list(c.items()):
    if v % 2 != 0:
        cnt += 1
print(cnt)
