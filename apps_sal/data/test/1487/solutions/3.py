s = input()
t = input()
l = len(s)
p = ''

c = 0
for i in range(l):
    if s[i] != t[i]:
        if c % 2 == 0:
            p += s[i]
        else:
            p += t[i]
        c += 1
    else:
        p += s[i]
        
if c % 2 == 1:
    print('impossible')
else:
    print(p)
