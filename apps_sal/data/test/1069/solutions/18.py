s = ''
s = input()
length = len(s)
temp = int(s[length - 2]) * 10 + int(s[length - 1])
if temp % 4 == 0:
    print('4')
else:
    print('0')
