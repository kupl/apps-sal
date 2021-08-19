s = str(input())
a = ''
for i in s:
    if i != 'B':
        a = a + i
    elif len(a) != 0:
        a = a[0:len(a) - 1]
print(a)
