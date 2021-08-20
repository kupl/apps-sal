import sys
import itertools
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


N = ir()
XY = [lr() for _ in range(N)]
XY = [x + y * 1j for (x, y) in XY]
cen_cand = []
'\nz = (ab(a-b).conjugete()) / (a.conjugate()*b-a*b.conjugate())\n'


def find_center(a, b, c):
    a -= c
    b -= c
    if abs((a * b.conjugate()).imag) < 0.5:
        return None
    num = a * b * (a - b).conjugate()
    den = a.conjugate() * b
    den -= den.conjugate()
    return num / den + c


for comb in itertools.combinations(XY, 3):
    o = find_center(*comb)
    if o is None:
        continue
    cen_cand.append(o)
for (a, b) in itertools.combinations(XY, 2):
    o = (a + b) / 2
    cen_cand.append(o)
cen_cand = np.array(cen_cand)
XY = np.array(XY)
answer = np.abs(cen_cand[:, None] - XY[None, :]).max(axis=1).min()
print(answer)
