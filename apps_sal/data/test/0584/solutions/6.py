n = int(input())
s = input()
swb = ''
opened = 0
sib = ''
for sym in s:
    if sym == '(':
        opened += 1
    if sym == ')':
        opened -= 1
    if opened == 0:
        if sym != '(' and sym != ')':
            swb += sym
        if sym == ')':
            swb += '_'
    if opened > 0:
        if sym != ')' and sym != '(':
            sib += sym
        if sym == '(':
            sib += '_'
t = swb.split('_')
print(max([len(elem) for elem in t]), end=' ')
t = sib.split('_')
t1 = []
for lem in t:
    if lem != '':
        t1.append(lem)
print(len(t1))
