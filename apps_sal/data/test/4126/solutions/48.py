s = input()
sf = s[:int((len(s) - 1) / 2)]
sl = s[int((len(s) + 3) / 2) - 1:]
if s == s[::-1] and sf == sf[::-1] and (sl == sl[::-1]):
    print('Yes')
else:
    print('No')
