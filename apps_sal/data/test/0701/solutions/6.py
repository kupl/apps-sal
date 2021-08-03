"""
Codeforces Round 256 Div 2 Problem B

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
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


# SOLUTION
s = read(0)
t = read(0)
resstr = ["need tree", "automaton", "array", "both"]
res = -1

ars = [0] * 26
art = [0] * 26
for i in list(s):
    ars[ord(i) - 97] += 1
for i in list(t):
    art[ord(i) - 97] += 1
for i in range(26):
    if art[i] > ars[i]:
        res = 0
        break
if not (res + 1):

    # automaton check
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    if j == len(t):
        res = 0
    else:
        res = 2

    if ars != art:
        res += 1
print(resstr[res])
