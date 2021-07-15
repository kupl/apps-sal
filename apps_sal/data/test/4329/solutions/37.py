s = input()

t = input()

i = len(t) - 1

if t == s + t[i]:
    print('Yes')
else:
    print('No')
