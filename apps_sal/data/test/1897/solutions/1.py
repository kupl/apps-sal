"""
Codeforces Contest 289 Div 2 Problem E

Author  : chaotic_iak
Language: Python 3.4.2
"""


def main():
    s = read(0)
    m = [1 if i in "AEIOUY" else 0 for i in s]
    n = len(m)
    m1 = [0]
    m2 = [0]
    for i in range(n):
        m1.append(m1[-1] + 1 / (1 + i))
        m2.append(m2[-1] + 1 / (n - i))
    mlast = m1[-1]
    for i in range(1, n + 1):
        m1[i] = m1[i - 1] + m1[i]
        m2[i] = m2[i - 1] + m2[i]
    sm = 0
    for i in range(n):
        sm += m[i] * ((i + 1) * mlast - m1[i] - m2[i])
    print(sm)


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
