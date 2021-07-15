import sys, math
s = input()
gg = 0
i = 0
dbl = 0
while i < len(s):
    if 'a' <= s[i] <= 'z':
        i += 1
        continue
    h = '000'
    while i < len(s) and  not 'a' <= s[i] <= 'z':
        h += s[i]
        i += 1
    ans = ''
    if h[-3] == '.':
        dbl += int(h[-2:])
        h = h[:-3] 
    for z in h:
        if z != '.':
            ans += z
    gg += int(ans)
#print(gg, dbl)
dd = []
gg += dbl // 100
dbl = dbl % 100
gg = gg
if dbl != 0:
    dbl = str(dbl)
    while len(dbl) < 2:
        dbl = '0' + dbl
    dd.append(dbl)
#print(dd)
if gg == 0:
    dd.append(0)
while gg != 0:
    dd.append(str(gg % 1000))
    if (gg >= 1000):
        while len(dd[-1]) < 3:
            dd[-1] = '0' + dd[-1]
    gg //= 1000
dd.reverse()
print(*dd, sep = '.')
    

    
            
        

