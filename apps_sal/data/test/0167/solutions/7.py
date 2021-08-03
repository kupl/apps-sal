import sys

s, t = input(), '*' + input()
n, m = len(s), len(t) - 1
inf = 10**9

pre, suf = [-1] + [inf] * (m + 1), [-1] * (m + 1) + [n]

i = 0
for j in range(1, m + 1):
    while i < n and s[i] != t[j]:
        i += 1
    if i == n:
        break
    pre[j] = i
    i += 1

i = n - 1
for j in range(m, 0, -1):
    while 0 <= i and s[i] != t[j]:
        i -= 1
    if i == -1:
        break
    suf[j] = i
    i -= 1

max_len, best_l, best_r = 0, 0, 0
j = 1
for i in range(m + 1):
    j = max(j, i + 1)
    while j <= m and pre[i] >= suf[j]:
        j += 1
    if pre[i] == inf:
        break
    if max_len < i + m + 1 - j:
        max_len = i + m + 1 - j
        best_l, best_r = i, j

pre_s = t[1:best_l + 1]
suf_s = t[best_r:]

print(pre_s + suf_s if max_len else '-')
