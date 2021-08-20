"""
Codeforces Contest 287 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.4.2
"""


def main():
    (r, x1, y1, x2, y2) = read()
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    import math
    return math.ceil(dist / 2 / r)


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
