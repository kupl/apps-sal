s = input()
t = ''
b = ''
a = ''
for i in range(len(s)):
    if not s[i] in [';', ',']:
        t += s[i]
    else:
        if t.isdigit() and (not (len(t) > 1 and t[0] == '0')):
            a += t + ','
        else:
            b += t + ','
        t = ''
if t.isdigit() and (not (len(t) > 1 and t[0] == '0')):
    a += t + ','
else:
    b += t + ','
if not len(a) == 0:
    print('"' + a[:-1] + '"')
else:
    print('-')
if not len(b) == 0:
    print('"' + b[:-1] + '"')
else:
    print('-')
