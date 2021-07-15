import sys


def input():
    return sys.stdin.readline().strip()


s = input()
n = len(s)

if n == 1:
    print(1)
    return

seq = [1]
for i in range(1, n):
    seq.append(seq[i - 1] + 1 if s[i] != s[i - 1] else 1)
ans = max(seq)
if ans == n:
    print(n)
    return

if s[0] != s[-1]:
    i = 1
    while i < n and s[i] != s[i - 1]:
        i += 1
    j = 1
    while j < n and s[n - 1 - j] != s[n - j]:
        j += 1
    ans = max(ans, i + j)
print(ans)

