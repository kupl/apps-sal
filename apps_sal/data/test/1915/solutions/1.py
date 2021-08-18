"""
Codeforces Contest 289 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.4.2
"""


from math import factorial as f


def main():
    n, = read()
    return f(2 * n - 2) // f(n - 1) // f(n - 1)


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


write(main())
