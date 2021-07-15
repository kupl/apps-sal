s = input()
if s[0]==s[-1]:
    a = 1
else:
    a = 0
if (len(s)-a)%2==0:
    print('Second')
else:
    print('First')
