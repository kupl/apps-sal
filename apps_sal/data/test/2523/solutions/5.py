import math


def f(s):
    if len(s) % 2 == 0:
        p = len(s) // 2 - 1
    else:
        p = len(s) // 2

    q = p
    while q < len(s) and s[p] == s[q]:
        q += 1
    return q


s = input()
l = len(s)
ans = l
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        ans = min(ans, max(i + 1, l - i - 1))
print(ans)
