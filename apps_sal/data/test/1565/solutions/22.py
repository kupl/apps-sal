import math
n = int(input())
s = input()
mini = math.inf
digits = 10 ** 5 + 10
for i in range(n // 2, n):
    if s[i] != '0':
        a = i
        b = n - i
        if max(a, b) > digits + 2:
            continue
        else:
            mini = min(mini, int(s[:i]) + int(s[i:]))
            digits = math.log10(mini) + 1
for i in range(n // 2 - 1, 0, -1):
    if s[i] != '0':
        a = i
        b = n - i
        if max(a, b) > digits + 2:
            continue
        else:
            mini = min(mini, int(s[:i]) + int(s[i:]))
            digits = math.log10(mini) + 1
print(mini)
