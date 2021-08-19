def task(n):
    (l, r) = n.partition('.')[::2]
    l = l.lstrip('0')
    exp = None
    if l:
        exp = len(l) - 1
        r = l[1:] + r
        l = l[0]
    else:
        strippedr = r.lstrip('0')
        exp = len(strippedr) - len(r) - 1
        l = strippedr[0]
        r = strippedr[1:]
    r = r.rstrip('0')
    return l + ('.%s' % r if r else '') + ('E%d' % exp if exp else '')


n = [input()]
for t in n:
    print(task(t))
