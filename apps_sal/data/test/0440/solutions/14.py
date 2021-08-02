b = input()
a = input()
c = []
g = 'aeiouy'
c.append(a[0])
for i in range(len(a) - 1):
    if a[i] in g and a[i + 1] in g:
        pass
    else:
        c.append(a[i + 1])


print(''.join(c))
