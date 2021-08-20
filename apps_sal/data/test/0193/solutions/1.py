"""
Codeforces Looksery Cup 2015 Problem H

Author  : chaotic_iak
Language: Python 3.4.2
"""


def minimize(m):
    ad = [m[0][0] * m[3][0], m[0][0] * m[3][1] + m[0][1] * m[3][0], m[0][1] * m[3][1]]
    bc = [m[1][0] * m[2][0], m[1][0] * m[2][1] + m[1][1] * m[2][0], m[1][1] * m[2][1]]
    det = [ad[0] - bc[0], ad[1] - bc[1], ad[2] - bc[2]]
    if det[0] != 0:
        disc = det[1] ** 2 - 4 * det[0] * det[2]
        if disc < 0:
            return []
        return [(-det[1] + disc ** 0.5) / (2 * det[0]), (-det[1] - disc ** 0.5) / (2 * det[0])]
    if det[1] != 0:
        return [-det[2] / det[1]]
    if det[2] != 0:
        return []
    return [0]


def main():
    matrix = read() + read()
    import itertools
    r = range(4)
    ans = 10 ** 18
    for i in range(5):
        for k in itertools.combinations(r, i):
            m = [(1 if j in k else -1, matrix[j]) for j in range(4)]
            for res in minimize(m):
                if abs(res) < ans:
                    ans = abs(res)
    print(ans)


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s='\n'):
    if s is None:
        s = ''
    if isinstance(s, list):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end='')


write(main())
