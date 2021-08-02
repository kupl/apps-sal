s = input()
o = s.find('^')
a = list(int(s[i]) if s[i].isdigit() else 0 for i in range(len(s)))
summa = 0
for i in range(len(s)):
    summa += (i - o) * a[i]
if summa < 0:
    print('left')
elif summa == 0:
    print('balance')
else:
    print('right')
