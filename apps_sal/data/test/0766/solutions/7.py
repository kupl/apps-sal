s = sorted(input())
t = 1
lets = []
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        t += 1
    else: 
        lets.append(t)
        t = 1
lets.append(t)
suc = False
if len(lets) == 2 and lets[0] > 1 and lets[1] > 1: suc = True
if len(lets) == 3 and max(lets) > 1: suc = True
if len(lets) == 4: suc = True
if suc: print('Yes')
else: print('No')

