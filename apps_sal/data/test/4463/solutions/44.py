s = str(input())
t = str(input())
a = ''.join(sorted(s))
b = ''.join(sorted(t, reverse=True))
if a < b:
    print('Yes')
else:
    print('No')
