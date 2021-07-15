n = int(input())
x = input()

def f(x):
    q, s = 0, 0
    for c in x:
        if c == '?':
            q += 1
        else:
            s += int(c)
    return q, s

lq, ls = f(x[:n//2])
rq, rs = f(x[n//2:])

lmin = ls
lmax = ls + 9*lq

rmin = rs
rmax = rs + 9*rq

lc = lmin+lmax
rc = rmin+rmax

if lc == rc and (lq+rq)%2 == 0:
    print("Bicarp")
else:
    print("Monocarp")

