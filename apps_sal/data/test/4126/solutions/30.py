s = input()
n = len(s)
s1 = s[:(n - 1) // 2]
s2 = s[(n + 3) // 2 - 1:n]
if s != s[::-1] or s1 != s1[::-1] or s2 != s2[::-1]:
    print('No')
else:
    print('Yes')
