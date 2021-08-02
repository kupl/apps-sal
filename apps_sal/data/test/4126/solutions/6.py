import sys
s = list(input())
r = list(reversed(s))
n = len(s)

for i in range(n):
    if s[i] != r[i]:
        print('No')
        return

s1 = s[:]

del s1[(n - 1) // 2:]
r1 = list(reversed(s1))

for i in range(len(s1)):
    if s1[i] != r1[i]:
        print('No')
        return

s2 = s[:]

del s2[:(n + 3) // 2 - 1]
r2 = list(reversed(s2))

for i in range(len(s2)):
    if s2[i] != r2[i]:
        print('No')
        return
print('Yes')
