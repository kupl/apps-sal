import sys
sys.setrecursionlimit(10000)
n=int(input())

vs = {}
for c in range(2, n+1):
    p = int(input())
    if p in vs:
        vs[p].append(c)
    else:
        vs[p] = [c]

def check(n):
    if n not in vs:
        return 1
    ch = vs[n]
    s = 0
    for c in ch:
        r = check(c)
        if r == -1:
            return -1
        s+=r
    if s >= 3:
        return 0
    return -1

print('Yes' if check(1) == 0 else 'No')
