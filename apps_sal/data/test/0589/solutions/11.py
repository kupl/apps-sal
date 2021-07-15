s = input()
l = []
n = '0123456789'
c = 1
z = True
tot = 1
for i in s:
    if i == '?':
        if z:
            c*=9
        else:
            c *= 10
    elif i in n:
        pass
    else:
        if i not in l:
            if z:
                c *= 9
                l.append(i)
            else:    
                c *= (10 - len(l))
                l.append(i)
    z = False
print(c)
