n = int(input())
s = list(input())
el = 0
while el + 1 < len(s):
    if s[el] in 'aeiouy' and s[el + 1] in 'aeiouy':
        del s[el + 1]
    else:
        el += 1
print(''.join(s))
