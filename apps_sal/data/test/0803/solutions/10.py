from math import *
n = int(input())
s = input().strip()
c = 0
k = 0
c = s.count('x')
k = s.count('X')
i = 0
otv = []
print(min(abs(n // 2 - c), abs(n // 2 - k)))
if n // 2 - c > n // 2 - k:
    while i < n and c != n // 2:
        if s[i] == 'X':
            otv += 'x'
            c += 1
        else:
            otv += s[i]
        i += 1
    for j in range(i, n):
        otv += s[j]
elif n // 2 - c < n // 2 - k:
    while i < n and k != n // 2:
        if s[i] == 'x':
            otv += 'X'
            k += 1
        else:
            otv += s[i]
        i += 1
    for j in range(i, n):
        otv += s[j]
else:
    for j in range(n):
        otv += s[j]
print(''.join(otv))
