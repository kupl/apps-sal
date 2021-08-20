import sys
from math import ceil, floor
c = [ceil(n ** 2 / 2) for n in range(40)]
f = [floor(n ** 2 / 2) for n in range(40)]
n = int(sys.stdin.readline())
s_cnt = 0
h_cnt = 0
for _ in range(n):
    (t, h) = sys.stdin.readline().split()
    if h == 'hard':
        h_cnt += 1
    else:
        s_cnt += 1
idx = 0
a = max(s_cnt, h_cnt)
b = min(s_cnt, h_cnt)
while c[idx] < a:
    idx += 1
while f[idx] < b:
    idx += 1
print(idx)
