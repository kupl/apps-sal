midsym = 'AHIMOoTUVvWwXxY'
sym = 'pqbd'

s = input()

if len(s) % 2 == 1:
    t = len(s) // 2
    if s[t] not in midsym:
        print('NIE')
        return
    s = s[:t] + s[t + 1:]

# print(s)

f = s[:int(len(s) / 2)]
l = s[int(len(s) / 2):]
l = l[::-1]
for k in range(len(f)):
    if f[k] not in midsym and f[k] not in sym:
        print('NIE')
        return
    if f[k] in midsym:
        if l[k] != f[k]:
            print('NIE')
            return
    if f[k] in sym:
        if f[k] == 'p' and l[k] == 'q':
            continue
        if f[k] == 'q' and l[k] == 'p':
            continue
        if f[k] == 'b' and l[k] == 'd':
            continue
        if f[k] == 'd' and l[k] == 'b':
            continue
        print('NIE')
        return
print('TAK')
