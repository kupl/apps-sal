s = input().strip()
i = 0
alph = 'abcdefjhigklmnopqrstuwvxyz'
ans = 0
while i < len(s):
    if s[i] in alph:
        i += 1
    else:
        j = i
        while j < len(s) and (s[j] in '1234567890' or s[j] == '.'):
            j += 1
        c = s[i:j]
        fl = False
        for k in range(len(c) - 1, -1, -1):
            if c[k] == '.':
                fl = True
                if len(c) - k - 1 == 3:
                    c += '00'
                break
        if not fl:
            c += '00'
        a = ''
        for k in c:
            if k != '.':
                a = a + k
        #print(a)
        ans += int(a)
        i = j
an = str(ans)
a = ''
if len(an) < 3:
    an = '0' * (3 - len(an)) + an
a += an[-1]
a += an[-2]
a += '.'
i = 0
#print(an)
for k in range(len(an) - 3, -1, -1):
    a += an[k]
    i += 1
    if i == 3 and k > 0:
        a += '.'
        i = 0
fl = False
if ans % 100 == 0:
    fl = True

for i in range(len(a) - 1, -1, -1):
    if not fl or i > 2:
        print(a[i], end='')



