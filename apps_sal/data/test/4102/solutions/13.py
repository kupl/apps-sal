d = {'0': '8', '3': '3', '4': '6', '5': '9',
     '6': '4', '7': '7', '8': '0', '9': '5'}
s = input()
s1 = ''.join(d[c] for c in reversed(s) if c in d)
if s == s1:
    print('Yes')
else:
    print('No')

