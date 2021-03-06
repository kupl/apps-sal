(s, t) = (input(), input())
(sx, tx) = (str(sorted(s)), str(sorted(t)))


def subset(s, t):
    i = 0
    for c in s:
        if c == t[i]:
            i += 1
        if i == len(t):
            break
    return i == len(t)


if sx == tx:
    print('array')
elif subset(s, t):
    print('automaton')
elif subset(sx, tx):
    print('both')
else:
    print('need tree')
