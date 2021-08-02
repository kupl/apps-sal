n = input()
s = input()

res = ''
v = False
for c in s:
    if c in 'aeiouy' and not v:
        v = True
        res += c
    if c not in 'aeiouy':
        if v:
            v = False
        res += c

print(res)
