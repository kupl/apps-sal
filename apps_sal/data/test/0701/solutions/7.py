def check(s1, s2):
    for i in s1 + s2:
        if s1.count(i) < s2.count(i):
            return 0
    return 1


def aut(s1, s2):
    a1 = a2 = 0
    while a2 < len(s2):
        if a1 == len(s1):
            return 0
        while s1[a1] != s2[a2]:
            a1 += 1
            if a1 == len(s1):
                return 0
        a2 += 1
        a1 += 1
    return 1


s1 = input()
s2 = input()
if sorted(s1) == sorted(s2):
    print('array')
elif aut(s1, s2):
    print('automaton')
elif check(s1, s2):
    print('both')
else:
    print('need tree')
