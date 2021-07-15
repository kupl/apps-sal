t = input()
s, d = set(), set()
p = {(len(t), 2)}

while p:
    m, x = p.pop()
    r = m + x

    for y in [x, 5 - x]:
        l = m - y
        q = (l, y)

        if q in d or l < 5 or t[l:m] == t[m:r]: continue
        s.add(t[l:m])

        d.add(q)
        p.add(q)

print(len(s))
print('\n'.join(sorted(s)))

