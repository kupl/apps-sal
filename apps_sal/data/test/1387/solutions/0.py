"""
Codeforces Contest Good Bye 2014 Contest Problem A

Author  : chaotic_iak
Language: Python 3.4.2
"""


def main():
    n, t = read()
    a = read()
    c = 1
    while c < t:
        c += a[c - 1]
    if c == t:
        print("YES")
    else:
        print("NO")


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
