from sys import stdin
from bisect import bisect_left as bl
n, m, ta, tb, k = list(map(int, stdin.readline().strip().split()))
s = list(map(int, stdin.readline().strip().split()))
s1 = list(map(int, stdin.readline().strip().split()))
ans = -1
for i in range(min(k + 1, n)):
    x = s[i] + ta
    ind = bl(s1, x)
    y = ind + k - i
    if y >= m:
        ans = -1
        break
    if s1[y] >= x:
        ans = max(s1[y] + tb, ans)
if n <= k:
    ans = -1
print(ans)
