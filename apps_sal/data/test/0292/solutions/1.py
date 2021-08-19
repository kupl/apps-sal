"""
Codeforces Contest 287 Div 2 Problem C

Author  : chaotic_iak
Language: Python 3.4.2
"""

# SOLUTION


def main():
    h, n = read()
    n -= 1
    n = bin(n)[2:]
    n = "0" * (h - len(n)) + n

    s = ""
    for i in range(h):
        if i and n[i - 1] == "0":
            s += "1" if n[i] == "0" else "0"
        else:
            s += n[i]

    ct = 0
    for i in range(h):
        ct += 1
        if s[i] == "1":
            ct += 2**(h - i) - 1
    print(ct)

# HELPERS


def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
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
