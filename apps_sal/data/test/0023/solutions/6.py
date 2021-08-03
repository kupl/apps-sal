from collections import Counter

a, b = input(), input()
if len(a) < len(b):
    print(''.join(sorted(a)[::-1]))
else:
    a = Counter(a)
    t = []
    for q in b:
        t.append(q)
        a[q] -= 1
        if a[q] < 0:
            break
    else:
        print(''.join(t))
        return
    s = ''
    while not s:
        d = t.pop()
        a[d] += 1
        for q, k in a.items():
            if k > 0 and s < q < d:
                s = q
    a[s] -= 1
    t.append(s)
    for q in '9876543210':
        t += [q] * a[q]
    print(''.join(t))
