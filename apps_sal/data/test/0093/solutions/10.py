s1 = ''
s2 = ''
for i in range(2):
    r = list(input())
    if i == 1:
        r = r[1] + r[0]
    for c in r:
        if c != 'X':
            s1 += c
for i in range(2):
    r = input()
    if i == 1:
        r = r[1] + r[0]
    for c in r:
        if c != 'X':
            s2 += c
s2 *= 2
k = 0
for i in range(3):
    if s1 == s2[i:i + 3]:
        k = 1
if k == 0:
    print('NO')
else:
    print('YES')
