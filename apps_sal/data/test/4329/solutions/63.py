s = input()
t = input()
if s == t[0:-1] and len(s) + 1 == len(t):
    print('Yes')
else:
    print('No')
