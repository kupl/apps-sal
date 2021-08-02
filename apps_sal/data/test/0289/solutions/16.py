from sys import stdin, stdout

a = stdin.readline().rstrip()
a = list(a)

vkCount = 0
change = False
if a[0:2] == list('KK'):
    change = True
    a[0] = 'V'
elif a[-2:] == list('VV'):
    change = True
    a[-1] = 'K'

i = 0
while i < len(a) - 2 and not change:
    if a[i:i + 3] == list('VVV'):
        a[i + 1] = 'K'
        change = True
    elif a[i:i + 3] == list('KKK'):
        a[i + 1] = 'V'
        change = True
    i += 1

for i in range(len(a) - 1):
    if a[i:i + 2] == list('VK'):
        vkCount += 1

print(vkCount)
