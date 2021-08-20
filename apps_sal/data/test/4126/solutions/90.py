s = input()
n = len(s)
f = s[:(n - 1) // 2]
l = s[1 + (n - 1) // 2:]
print('Yes' if s == s[::-1] and f == f[::-1] and (l == l[::-1]) else 'No')
