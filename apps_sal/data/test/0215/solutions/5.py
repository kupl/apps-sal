n = input()
s = input()
z = ''
for c in s:
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        z += c
    else:
        z += ' '
z = z.split(' ')
alp = range(26)
res = 0
for w in z:
    kek = 26
    for x in alp:
        if w.find(chr(ord('a') + x)) == -1:
            kek -= 1
    res = max(res, kek)
print(res)
