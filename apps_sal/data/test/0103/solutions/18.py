from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial

n = int(stdin.readline())
vl = list(map(int, stdin.readline().split()))
ans = 0

for i in range(n):
    cnt = 0
    while i + cnt < n and vl[i + cnt] == vl[i] + cnt:
        cnt += 1

    ans = max(ans, cnt - 2)


cnt1 = 0
while cnt1 < n and vl[cnt1] == cnt1 + 1:
    cnt1 += 1

cnt2 = 0
while cnt2 < n and vl[n - 1 - cnt2] == 10 ** 3 - cnt2:
    cnt2 += 1

ans = max(ans, max(cnt1, cnt2) - 1)
stdout.write(str(ans))
