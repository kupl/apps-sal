s = input()
a = False
b = False
c = False
d = False
if len(s) >= 5:
    a = True
for i in range(len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        b = True
    if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
        c = True
    if ord(s[i]) >= ord('1') and ord(s[i]) <= ord('9'):
        d = True
if a and b and c and d:
    print('Correct')
else:
    print('Too weak')
