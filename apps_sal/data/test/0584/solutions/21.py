input()
s = input()
f = False
a = []
for c in s:
    if c == '(':
        f = True
    if f == False:
        a.append(c)
    if c == ')':
        f = False
        a.append('_')
a = ''.join(a)
b = [len(s) for s in a.split('_') if s != ''] + [0]
c = sorted(b)[-1]
al = len(b) - 1
d = s.replace('_', ' ').replace('(', ' ').replace(')', ' ')
d = d.split()
print(c, len(d) - al, end=' ')
