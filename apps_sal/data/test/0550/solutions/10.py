import sys


equiv = {
    'o': 1, 'O': 1, '0': 1,
    '1': 2, 'l': 2, 'L': 2, 'i': 2, 'I': 2
}


def compare(c1, c2):
    if ord(c1) > ord(c2):
        c1, c2 = c2, c1

    e1, e2 = equiv.get(c1, 0), equiv.get(c2, 0)
    if e1 and e2 and e1 == e2:
        return True

    if 'A' <= c1 <= 'Z' and chr(ord(c1) - ord('A') + ord('a')) == c2:
        return True
    
    return c1 == c2


def cmps(s1, s2):
    if len(s1) != len(s2):
        return False

    for c1, c2 in zip(s1, s2):
        if not compare(c1, c2):
            return False

    return True


s = input()
n = int(input())

for _ in range(n):
    s_i = input()
    if cmps(s_i, s):
        print("No")
        return

print("Yes")

