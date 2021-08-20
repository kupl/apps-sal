n = input()
s = input()
if len(s) == 1:
    print('Yes')
elif len(s) == len(set(s)):
    print('No')
else:
    print('Yes')
