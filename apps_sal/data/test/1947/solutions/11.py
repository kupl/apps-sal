n, m, l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

def time_to_cut():
    nonlocal a
    t = 0
    pr = 0
    for i in range(n):
        if a[i] <= l:
            pr = 0
        elif pr == 0:
            t += 1
            pr = 1
    return(t)

def update_time(p, d):
    nonlocal a
    nonlocal T
    p -= 1
    pos = (0 if a[p] <= l else 1)
    a[p] += d
    pns = (0 if a[p] <= l else 1)
    sa = bool(pns - pos)
    if not sa:
        pass
    elif n == 1:
        T += 1
    elif p == 0:
        if a[p+1] <= l:
            T += 1
    elif p == n-1:
        if a[p-1] <= l:
            T += 1
    elif a[p+1] <= l and a[p-1] <= l:
        T += 1
    elif a[p+1] > l and a[p-1] > l:
        T -= 1
    return

T = time_to_cut()

for i in range(m):
    r = [int(x) for x in input().split()]
    if len(r) == 1: # time request
        print(T)
    else: # hair grow
        update_time(r[1], r[2])

