s = input()
t = input()
a = len(s)
b = 0
for i in range(a):
    if s == t:
        b += 1
        break
    else:
        c = s[-1]
        s = c + s[:-1]

if b == 1:
    print('Yes')
else:
    print('No')
