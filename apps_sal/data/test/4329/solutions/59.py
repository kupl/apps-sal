n = input()
s = input()
if n == s[:-1] and len(n) == len(s) - 1:
    print('Yes')
else:
    print('No')
