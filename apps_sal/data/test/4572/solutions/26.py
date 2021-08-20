s = set(input())
a = 'abcdefghijklmnopqrstuvwxyz'
for si in s:
    a = a.replace(si, '')
print(None if a == '' else a[0])
