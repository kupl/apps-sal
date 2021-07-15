s = input()
a = [0]*len(s)
if int(s[0])>=5:
    if int(s[0])!=9:
        a[0] = 9-int(s[0])
    else:
        a[0] = int(s[0])
else:
    a[0] = int(s[0])
for i in range(1, len(s)):
    if int(s[i])>=5:
        a[i] = 9 - int(s[i])
    else:
        a[i] = int(s[i])
print(''.join(map(str, a)))
