from functools import cmp_to_key
n = int(input())
strings = [input() for i in range(n)]
'\ndef cmp(s1, s2):\n    l = min(len(s1), len(s2))\n    for i in range(l):\n        if s1[i] < s2[i]:\n            return -1\n        elif s1[i] > s2[i]:\n            return 1\n    if len(s1) < len(s2):\n        return ord(s1[0]) - ord(s2[l])\n    elif len(s1) > len(s2):\n        return ord(s1[l]) - ord(s2[0])\n    return 0\n'


def cmp(s1, s2):
    (z1, z2) = (s1 + s2, s2 + s1)
    if z1 < z2:
        return -1
    elif z2 > z1:
        return 1
    else:
        return 0


strings.sort(key=cmp_to_key(cmp))
for string in strings:
    print(string, end='')
print('')
