def chk(l1, l2, known_keys):
    if l1 not in known_keys and l2 not in known_keys:
        known_keys[l1] = l2
        known_keys[l2] = l1
    elif l1 in known_keys and known_keys[l1] != l2 or (l2 in known_keys and known_keys[l2] != l1):
        raise ValueError('bad kbd')


def m():
    keys = {}
    s1 = input()
    s2 = input()
    try:
        for i in map(lambda x, y: chk(x, y, keys), s1, s2):
            pass
    except ValueError:
        print(-1)
        return
    k1 = list([x for x in keys if ord(x) < ord(keys[x])])
    print(len(k1))
    for k in k1:
        print(k, keys[k])


def __starting_point():
    m()


__starting_point()
