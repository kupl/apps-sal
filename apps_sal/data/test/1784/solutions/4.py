"""
Codeforces Contest 289 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.4.2
"""


def main():
    n, k = read()
    a = read()
    if max(a) - min(a) > k:
        return "NO"
    print("YES")
    for i in a:
        print("1 " * min(a) + " ".join(map(str, range(1, i - min(a) + 1))))


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
