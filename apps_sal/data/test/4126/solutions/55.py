s = input()
n = len(s)
s_ = s[:(n - 1) // 2]
if s == s[::-1] and s_ == s_[::-1]:
    print('Yes')
else:
    print('No')
