a = input()
b = input()
i = 0
while i < len(a) and a[i] == '0':
    i += 1
j = 0
while j < len(b) and b[j] == '0':
    j += 1
a = a[i:]
if a == '':
    a = '0'
b = b[j:]
if b == '':
    b = '0'
if len(a) > len(b):
    print('>')
elif len(b) > len(a):
    print('<')
else:
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    if i == len(a):
        print('=')
    elif a[i] > b[i]:
        print('>')
    else:
        print('<')
