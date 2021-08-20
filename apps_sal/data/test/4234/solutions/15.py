import os
import sys


def log(*args, **kwargs):
    if os.environ.get('CODEFR'):
        print(*args, **kwargs)


n = int(input())
s = input()
result = ''
i = 0
while i < n - 1:
    j = i + 1
    while j != n:
        if s[i] != s[j]:
            result += s[i] + s[j]
            i = j + 1
            break
        j += 1
    if j == n:
        break
print(n - len(result))
print(result)
