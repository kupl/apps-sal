"""
Codeforces Round 253 Div 1 Problem B

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
    if mode == 3:
        return [float(x) for x in inputs.split()]


def write(s="\n"):
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


n, = read()
s = read(3)
s.sort(reverse=True)
s = [int(10**6 * i + 0.5) for i in s]
onewin = s[0]
alllose = 10**6 - s[0]
ct = 1
while alllose > onewin and ct < n:
    onewin = onewin * (10**6 - s[ct]) + alllose * s[ct]
    alllose *= (10**6 - s[ct])
    ct += 1
print(onewin / 10**(6 * ct))
