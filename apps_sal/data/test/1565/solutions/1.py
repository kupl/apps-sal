import math


def f(R):
    if R == 0:
        return 0
    F = 0
    S = 0
    cur = 1
    for i in range(150):
        t = min(cur, R - F - S)
        if i % 2 == 0:
            F = F + t
        else:
            S = S + t
        cur = cur * 2
        if R == F + S:
            break
    ans = F * F + S * S + S
    return ans


n = int(input())
s = input()
ans = int(s)
for i in range(n // 2, n):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
for i in range(n // 2, 0, -1):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
for i in range(n // 2 + 1, n):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
for i in range(n // 2 + 1, 0, -1):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
print(ans)
