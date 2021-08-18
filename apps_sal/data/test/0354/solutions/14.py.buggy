import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()

if len(s) != len(t):
    print('No')
    return

vow = set(['a', 'e', 'i', 'o', 'u'])

valid = True
for i in range(len(s)):
    if s[i] in vow and not t[i] in vow:
        valid = False
        break
    if t[i] in vow and not s[i] in vow:
        valid = False
        break

if valid:
    print('Yes')
else:
    print('No')
