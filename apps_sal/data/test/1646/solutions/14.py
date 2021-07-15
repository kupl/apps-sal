n = int(input())
s = input()

o = s.count('1')
z = s.count('0')

if s == '0':
    print('0')
else:
    print('1'+'0'*z)

