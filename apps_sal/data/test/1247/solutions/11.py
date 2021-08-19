(t, p) = (input(), {})
for i in t:
    p[i] = p.get(i, 0) + 1
s = sum((p[i] % 2 for i in p))
if s < 2:
    print('First')
elif s % 2 == 0:
    print('Second')
else:
    print('First')
