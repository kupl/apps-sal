a = input()
b = 0
c = '([{<'
d = ')]}>'
e = []
f = False
for i in a:
    if i in c: e += [i]
    else:
        if not e:
            print('Impossible')
            f = True
            break
        if d.index(i) != c.index(e[-1]): b += 1
        e.pop()
if e: print('Impossible')
elif not f: print(b)
