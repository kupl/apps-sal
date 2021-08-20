from collections import defaultdict as dd, deque
q = int(input())


def solve():

    def f(x):
        C = dd(int)
        for a in x:
            C[a] += 1
        return C
    s = input()
    t = input()
    p = input()
    cs = f(s)
    ct = f(t)
    cp = f(p)
    needed = dd(int)
    for k in ct:
        needed[k] += ct[k]
    for k in cs:
        needed[k] -= cs[k]
    for k in needed:
        if needed[k] > cp[k] or needed[k] < 0:
            return False
    i = 0
    j = 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
            j += 1
        else:
            if ct[t[j]] > 0:
                ct[t[j]] -= 1
            else:
                return False
            j += 1
    return i == len(s) and j == len(t)


for _ in range(q):
    if solve():
        print('YES')
    else:
        print('NO')
