def contain(s, t):
    s = list(s)
    p = list(s)
    for i in t:
        if i in s:
            s.remove(i)
        else:
            return False
    return True


def find(s, t):
    t = list(t)
    j = 0
    while j < len(s):
        if t[0] == s[j]:
            t.pop(0)
            if len(t) == 0:
                return True
        j += 1
    return len(t) == 0


s = input()
t = input()
if find(s, t):
    print('automaton')
elif contain(s, t) and len(s) > len(t):
    print('both')
elif contain(s, t) and len(s) == len(t):
    print('array')
else:
    print('need tree')
