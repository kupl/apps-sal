import re
s = input().strip()
for i in range(0, len(s)):
    for j in range(i + 1, len(s) + 1):
        if s[:i] + s[j:] == 'CODEFORCES':
            print('YES')
            raise SystemExit
print('NO')
