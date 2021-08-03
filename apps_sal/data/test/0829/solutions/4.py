n = int(input())
s = input()
a = s.count('0')
b = s.count('1')
if a == b:
    print(2)
    print(s[0] + ' ' + s[1:])
else:
    print(1)
    print(s)
