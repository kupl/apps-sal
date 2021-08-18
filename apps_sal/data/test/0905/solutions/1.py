"""
Codeforces Contest 264 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""


def main():
    n, s = read()
    mx = -1
    for i in range(n):
        x, y = read()
        if y == 0 and x <= s:
            mx = max(0, mx)
        elif x < s:
            mx = max(100 - y, mx)
    print(mx)


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
