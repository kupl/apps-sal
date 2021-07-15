s = input()
t = s.count('1')
s = s.replace('1', '')

i = s.find('2')
if i == -1:
    print(s + '1'*t)
else:
    print(s[:i] + '1'*t + s[i:])

