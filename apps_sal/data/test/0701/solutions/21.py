def can_with_automaton(src, dst):
    sr = list(src)
    ds = list(dst)
    while ds and sr:
        if ds[-1] == sr[-1]:
            ds.pop()
        sr.pop()
    return bool(not ds)


def can_with_array(src, dst):
    return sorted(src) == sorted(dst)


def can_with_both(src, dst):
    for l in dst:
        if src.count(l) < dst.count(l):
            return False
    return True


s = input()
t = input()
if can_with_automaton(s, t):
    print('automaton')
elif can_with_array(s, t):
    print('array')
elif can_with_both(s, t):
    print('both')
else:
    print('need tree')
