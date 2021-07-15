from sys import stdin, stdout
from math import factorial
from math import log10
from math import sqrt

n = int(stdin.readline())
values = sorted(list(map(int, stdin.readline().split())))


cur = 1
cnt = 0
for v in values:
    cnt += abs(v - cur)
    cur += 2

ans = cnt

cur = 2
cnt = 0

for v in values:
    cnt += abs(v - cur)
    cur += 2

ans = min(ans, cnt)

stdout.write(str(ans))
