s = input()
t = input()
 
if len(s) + 1 == len(t) and s in t and s[0] == t[0]:
    print('Yes')
else: 
    print('No')
