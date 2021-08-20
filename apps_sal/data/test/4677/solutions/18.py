s = input()
a = ''
for i in range(len(s)):
    if s[i] == 'B':
        a = a[:-1]
    else:
        a += s[i]
print(a)
