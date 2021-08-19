s = input()
c = 0
a = []
i = 0
b = 0
while c < len(s):
    if s[i] not in a:
        x = s.count(s[i])
        if x % 2 == 1:
            b += 1
        c += x
        a.append(s[i])
    i += 1
if b == 0 or b % 2 == 1:
    print('First')
else:
    print('Second')
