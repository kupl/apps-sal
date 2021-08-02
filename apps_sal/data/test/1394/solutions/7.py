from collections import Counter


def func(s):
    res = []
    for c in s:
        if c != 'a':
            res.append(c)
    return ''.join(res)


s = input()
n = len(s)
c = Counter(list(s))
m = n - c['a']

if m % 2 != 0:
    print(':(')
else:
    t = s[:m // 2 + c['a']]
    if func(t) == s[m // 2 + c['a']:]:
        print(t)
    else:
        print(':(')
