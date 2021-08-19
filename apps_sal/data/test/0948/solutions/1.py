"""
Codeforces Looksery Cup 2015 Problem A

Author  : chaotic_iak
Language: Python 3.4.2
"""


def main():
    (n, m) = read()
    s = []
    for i in range(n):
        s.append(read(0))
    ans = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if {s[i][j], s[i][j + 1], s[i + 1][j], s[i + 1][j + 1]} == set('face'):
                ans += 1
    return ans


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
