"""
Codeforces Round 252 Div 2 Problem A

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


def write(s='\n'):
    if isinstance(s, list):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end='')


(k, v) = read()
res = []
for i in range(k):
    a = read()
    n = a.pop(0)
    if min(a) < v:
        res.append(i + 1)
print(len(res))
write(res)
