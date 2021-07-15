a = dict()
b = dict()
a1 = 'qwertyuiopasdfghjkl;zxcvbnm,./'
for i in range(len(a1)):
    a[a1[i]] = i
    b[i] = a1[i]
direct = input().strip()
if direct == 'L':
    direct = 1
else:
    direct = -1
s = input().strip()
for i in range(len(s)):
    print(b[a[s[i]]+direct], end = '')
