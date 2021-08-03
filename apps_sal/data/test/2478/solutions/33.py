_, S, l, r = input(), input(), '(', ')'
t = S
while t.count(l + r):
    t = t.replace(l + r, '')
print(l * t.count(r) + S + r * t.count(l))
