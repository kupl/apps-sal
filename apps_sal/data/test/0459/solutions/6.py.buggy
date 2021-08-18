import itertools
import sys
id = '''
  12
  34
ef56ijmn
gh78klop
  9a
  bc
'''

transforms = [
    [
        [1, 2, 3, 4],
        [22, 21, 18, 17, 6, 5, 14, 13]
    ],
    [
        [9, 10, 11, 12],
        [15, 16, 7, 8, 19, 20, 23, 24],
    ],
    [
        [5, 6, 7, 8],
        [3, 4, 17, 19, 10, 9, 16, 14],
    ],
    [
        [13, 14, 15, 16],
        [1, 3, 5, 7, 9, 11, 24, 22],
    ],
    [
        [17, 18, 19, 20],
        [4, 2, 21, 23, 12, 10, 8, 6],
    ],
    [
        [21, 22, 24, 23],
        [2, 1, 13, 15, 11, 12, 20, 18]
    ],
]


def rot(c, perm, rev):
    new = list(c)
    if rev:
        for i in range(len(perm)):
            new[perm[i] - 1] = c[perm[(i + 1) % len(perm)] - 1]
    else:
        for i in range(len(perm)):
            new[perm[(i + 1) % len(perm)] - 1] = c[perm[i] - 1]
    return new


def do_t(c, t, rev):
    return rot(rot(rot(c, t[0], rev), t[1], rev), t[1], rev)


faces = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
colors = input().split()

for rev, t in itertools.product([0, 1], transforms):
    newc = do_t(colors, t, rev)
    ok = True
    for f in faces:
        fc = [newc[i - 1] for i in f]
        if fc.count(fc[0]) != 4:
            ok = False

    if ok:
        #print('rotate', rev, t)
        print('YES')
        return

print('NO')
