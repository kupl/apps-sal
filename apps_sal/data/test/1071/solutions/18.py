"""
Codeforces Round 256 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return [int(x) for x in inputs.split()]


def write(s="\n"):
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


a = sum(read())
b = sum(read())
n, = read()
if -(-a // 5) - (-b // 10) > n:
    print("NO")
else:
    print("YES")
