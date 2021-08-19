from sys import *
from math import *
s = stdin.readline().strip()
ans = 1
now = 10
was = {}
was['A'] = False
was['B'] = False
was['C'] = False
was['D'] = False
was['E'] = False
was['F'] = False
was['G'] = False
was['H'] = False
was['I'] = False
was['J'] = False
if s[0] == '?':
    ans *= 9
if ord(s[0]) >= ord('A') and ord(s[0]) <= ord('J'):
    ans *= 9
    was[s[0]] = True
    now = 9
for i in range(1, len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('J'):
        if was[s[i]] == False:
            ans *= now
            now -= 1
        was[s[i]] = True
    elif s[i] == '?':
        ans *= 10
print(ans)
