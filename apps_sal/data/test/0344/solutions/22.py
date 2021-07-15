s = input() + 'd'
n = len(s)
glas = set(('a', 'o', 'u', 'i', 'e'))
f = True
for i in range(n - 1):
    if s[i] in glas or s[i] == 'n':
        continue
    if s[i + 1] not in glas:
        f = False
if f:
    print('YES')
else:
    print('NO')
