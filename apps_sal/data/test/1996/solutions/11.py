n = int(input())
alf = 'abcdefghijklmnopqrstuvwxyz'
so = ''
j = n
for i in range(n):
    s = input()
    j -= 1
    if s[0] == '!':
        so = ''
        for e in alf:
            if s.find(e) > -1:
                so += e
        alf = so
    elif s[0] == '.':
        so = ''
        for e in alf:
            if s.find(e) == -1:
                so += e
        alf = so
    else:
        alf = alf.replace(s[2], '')
    if len(alf) == 1:
        break
lol = 0
p = j
for i in range(j - 1):
    s = input()
    if s[0] == '!' or s[0] == '?':
        lol += 1
if not(p == 0):
    s = input()
print(lol)
