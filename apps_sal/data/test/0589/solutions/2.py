
s = input()
x = set()
f = False
r = 1
letter = set([c for c in 'ABCDEFGHIJ'])
if s[0] == '?':
    r *= 9
if s[0] in letter:
    x.add(s[0])
    f = True
for c in s[1:]:
    if c == '?':
        r *= 10
    if c in letter:
        x.add(c)
for t in range(len(x)):
    if t == 0 and f:
        r *= 9
    else:
        r *= 10 - t

print(r)
