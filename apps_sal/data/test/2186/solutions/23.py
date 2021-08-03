'''

@author: ChronoCorax
'''

seed = 201
div = 9999999999999983

ABC = ['a', 'b', 'c']


def hashi(s):
    L = len(s)
    h = 0
    pseed = 1
    for i in range(L):
        h, pseed = (h + ord(s[i]) * pseed) % div, (pseed * seed) % div
    return h


n, m = [int(c) for c in input().split()]

S = set()

for _ in range(n):
    s = input()
    L = len(s)

    hashs = hashi(s)

    pseed = 1
    for i in range(L):
        orig = s[i]
        for c in ABC:
            if c == orig:
                continue
            S.add((hashs + pseed * (ord(c) - ord(orig)) + div) % div)
        pseed = (pseed * seed) % div


res = []
for _ in range(m):
    hi = hashi(input())
    if hi in S:
        res.append('YES')
    else:
        res.append('NO')

print('\n'.join(res))
