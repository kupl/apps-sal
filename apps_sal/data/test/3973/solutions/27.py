from collections import Counter
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
(n, m) = [int(item) for item in input().split()]
a = [int(item) - 1 for item in input().split()]
cnt_t = [0] * m
ans = [0] * m
cnt_r = [0] * (m + 1)
for (a1, a2) in zip(a, a[1:]):
    ans[0] += min((m + a2 - a1) % m, (m + a2 - 0) % m + 1)
    cnt_t[a2] += (m + a2 - a1) % m - 1
    if (m + a2 - a1) % m <= 1:
        continue
    add = (a1 + 2) % m
    sub = a2 + 1
    if add < sub:
        cnt_r[add] += 1
        cnt_r[sub] -= 1
    else:
        cnt_r[add] += 1
        cnt_r[sub] -= 1
        cnt_r[0] += 1
        cnt_r[m] -= 1
for i in range(m):
    cnt_r[i + 1] += cnt_r[i]
for i in range(1, m):
    ans[i] = ans[i - 1] - cnt_r[i] + cnt_t[i - 1]
print(min(ans))
