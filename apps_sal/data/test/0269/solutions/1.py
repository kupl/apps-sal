import sys
s = input()
n = len(s)
ans = [0] * 4
a = s.index('R') % 4
for i in range(a, n, 4):
    if s[i] != 'R':
        ans[0] += 1
a = s.index('B') % 4
for i in range(a, n, 4):
    if s[i] != 'B':
        ans[1] += 1
a = s.index('Y') % 4
for i in range(a, n, 4):
    if s[i] != 'Y':
        ans[2] += 1
a = s.index('G') % 4
for i in range(a, n, 4):
    if s[i] != 'G':
        ans[3] += 1
print(*ans)
