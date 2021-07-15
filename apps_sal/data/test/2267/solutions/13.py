from functools import cmp_to_key

n = int(input())
strings = [input() for i in range(n)]

"""
def cmp(s1, s2):
    l = min(len(s1), len(s2))
    for i in range(l):
        if s1[i] < s2[i]:
            return -1
        elif s1[i] > s2[i]:
            return 1
    if len(s1) < len(s2):
        return ord(s1[0]) - ord(s2[l])
    elif len(s1) > len(s2):
        return ord(s1[l]) - ord(s2[0])
    return 0
"""

def cmp(s1, s2):
    z1, z2 = s1 + s2, s2 + s1
    if z1 < z2:
        return -1
    elif z2 > z1:
        return 1
    else:
        return 0

strings.sort(key=cmp_to_key(cmp))
for string in strings:
    print(string, end="")
print("")
