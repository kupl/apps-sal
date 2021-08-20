s = input()
s = s[1:-1]
if s == '':
    print('0')
else:
    a = s.split(', ')
    print(len(set(a)))
