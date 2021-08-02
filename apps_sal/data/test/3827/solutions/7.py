import re


def sv():
    S = input()
    if not re.match(r'^a+b+c+$', S):
        return False
    chrs = {'a': 0, 'b': 0, 'c': 0}
    for c in S:
        chrs[c] += 1
    return chrs['c'] == chrs['a'] or chrs['c'] == chrs['b']


print('YES' if sv() else 'NO')
