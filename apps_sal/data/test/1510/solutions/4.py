"""
Codeforces Round 251 Div 2 Problem D

Author  : chaotic_iak
Language: Python 3.3.4
"""


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
        return [int(x) for x in inputs.split()]


def write(s="\n"):
    if isinstance(s, list): s = " ".join(s)
    s = str(s)
    print(s, end="")


# SOLUTION
n, m = read()
a = read()
b = read()
s = [0] + a + b
s.sort()
t = sum(b)
mn = t
for i in range(n + m):
    t += (i - m) * (s[i + 1] - s[i])
    mn = min(mn, t)
print(mn)
