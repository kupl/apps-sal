(t, p) = (input(), [])
(n, k, x) = (0, True, t[0])
for i in t[1:] + ' ':
    if i == x:
        n += 1
    else:
        if n and k:
            p += [x, x]
            k = False
        else:
            p.append(x)
            k = True
        (x, n) = (i, 0)
print(''.join(p))
