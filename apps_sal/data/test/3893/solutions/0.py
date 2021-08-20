"""
Codeforces Contest 284 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.4.2
"""


def main():
    (x1, y1) = read()
    (x2, y2) = read()
    (n,) = read()
    ct = 0
    for i in range(n):
        (a, b, c) = read()
        if (a * x1 + b * y1 + c) * (a * x2 + b * y2 + c) < 0:
            ct += 1
    print(ct)


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
