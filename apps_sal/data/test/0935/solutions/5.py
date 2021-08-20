"""
Codeforces Contest 258 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""


def main():
    res_str = ['Malvika', 'Akshat']
    (n, m) = read()
    print(res_str[min(n, m) % 2])


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return map(int, inputs.split())


def read_str():
    return read(0)


def read_int():
    return read(1)


def write(s='\n'):
    if isinstance(s, list):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end='')


main()
