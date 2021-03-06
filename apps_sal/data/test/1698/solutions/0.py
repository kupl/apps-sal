"""
Codeforces Contest 270 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


def main():
    (n, k) = read()
    a = [i - 1 for i in read()]
    a.sort()
    a.reverse()
    print(sum(a[::k]) * 2)


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
