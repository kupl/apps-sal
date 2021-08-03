# s = "tessts"
# t = "tet"
from collections import defaultdict
s = input()
t = input()
ns = len(s)
nt = len(t)

ans = 0
found = 0

DP_left = [0] * ns

DP_left[0] = int(s[0] == t[0])
for i in range(1, ns):
    if DP_left[i - 1] < nt:
        DP_left[i] = DP_left[i - 1] + (s[i] == t[DP_left[i - 1]])

DP_right = [0] * ns

DP_right[-1] = int(s[-1] == t[-1])

for i in reversed(list(range(ns - 1))):
    if 0 <= nt - DP_right[i + 1] - 1 < nt:
        DP_right[i] = DP_right[i + 1] + (s[i] == t[nt - 1 - DP_right[i + 1]])


d_r = defaultdict(int)
d_l = defaultdict(int)

old = 1

for index, i in enumerate(DP_left):
    if i == old:
        d_l[i] = index
        old += 1

for index, i in enumerate(DP_right):
    d_r[i] = max(d_r[i], index)

for i in range(nt + 1):

    if i == 0:
        ans = max(ans, d_r[nt])
    elif i == nt:
        ans = max(ans, ns - d_l[nt] - 1)
    else:
        ans = max(ans, d_r[nt - i] - d_l[i] - 1)
print(ans)
