n = int(input())
s = input()
if '1' not in s:
    print('0')
else:
    print('1' + '0' * s.count('0'))
