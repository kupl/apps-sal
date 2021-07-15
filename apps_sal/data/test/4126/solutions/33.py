s = input()
n = len(s) // 2

if s[:n] == s[n+1:]:
    print('Yes')
else:
    print('No')

