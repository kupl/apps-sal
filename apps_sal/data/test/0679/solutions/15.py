s = input().strip()
f = False
for i in range(len(s) - 2):
    if s[i] != s[i + 1] and s[i] != s[i + 2] and (s[i + 1] != s[i + 2]) and (s[i] != '.') and (s[i + 1] != '.') and (s[i + 2] != '.'):
        f = True
if f:
    print('Yes')
else:
    print('No')
