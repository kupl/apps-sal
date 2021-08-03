n = int(input())
s = input()
s = list(s)
v = 0
while(True):
    lExits = False
    rExits = False
    if ('L' in s):
        l = s.index('L')
        lExits = True
    if ('R' in s):
        r = s.index('R')
        rExits = True
    if (lExits == False and rExits == False):
        break
    if (lExits == True and rExits == False):
        for i in range(l + 1):
            s[i] = 'F'
        break
    if (lExits == False and rExits == True):
        for i in range(r, n):
            s[i] = 'F'
        break
    if (lExits == True and rExits == True):
        if (l < r):
            for i in range(l + 1):
                s[i] = 'F'
        else:
            for i in range(r, l + 1):
                s[i] = 'F'
            if ((l - r) % 2 == 0):
                s[r] = '.'
c = 0
for i in s:
    if (i == '.'):
        c += 1
print(c)
