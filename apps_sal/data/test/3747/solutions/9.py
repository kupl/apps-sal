3
secret = 'Bulbasaur'
d = dict()
for c in secret:
    if c not in d:
        d[c] = 0
    d[c] += 1
s = input()
e = dict()
for c in s:
    if c not in e:
        e[c] = 0
    e[c] += 1
answ = 1791791791
for c in list(d.keys()):
    if c not in e:
        answ = 0
    else:
        answ = min(answ, e[c] // d[c])
print(answ)
