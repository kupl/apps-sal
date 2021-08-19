import sys
from collections import Counter
readline = sys.stdin.readline
Q = int(readline())
D0 = set()
D1 = set()
geta = 36


def tadd(x):
    bx = [1 if s == '1' else 0 for s in bin(x)[2:].zfill(34)]
    cur = 0
    for i in range(34):
        b = bx[i]
        (nw, dep) = divmod(cur, geta)
        if b == 1:
            if cur in D1:
                cur = ((nw << 1) + 1) * geta + dep + 1
                continue
            D1.add(cur)
            cur = ((nw << 1) + 1) * geta + dep + 1
            continue
        else:
            if cur in D0:
                cur = (nw << 1) * geta + dep + 1
                continue
            D0.add(cur)
            cur = (nw << 1) * geta + dep + 1
            continue


def trem(x):
    cur = x * geta + 34
    for i in range(34 - 1, -1, -1):
        (nw, dep) = divmod(cur, geta)
        if nw & 1:
            cur = (nw >> 1) * geta + dep - 1
            D1.remove(cur)
            if cur in D0:
                break
        else:
            cur = (nw >> 1) * geta + dep - 1
            D0.remove(cur)
            if cur in D1:
                break


def calc(x):
    bx = [1 if s == '1' else 0 for s in bin(x)[2:].zfill(34)]
    cur = 0
    for i in range(34):
        (nw, dep) = divmod(cur, geta)
        if bx[i] == 0:
            if cur in D1:
                cur = ((nw << 1) + 1) * geta + dep + 1
            else:
                cur = (nw << 1) * geta + dep + 1
        elif cur in D0:
            cur = (nw << 1) * geta + dep + 1
        else:
            cur = ((nw << 1) + 1) * geta + dep + 1
    return cur // geta ^ x


C = Counter()
Ans = []
tadd(0)
for _ in range(Q):
    (t, x) = readline().split()
    x = int(x)
    if t == '+':
        C[x] += 1
        if C[x] == 1:
            tadd(x)
    elif t == '-':
        C[x] -= 1
        if C[x] == 0:
            trem(x)
    else:
        Ans.append(calc(x))
print('\n'.join(map(str, Ans)))
