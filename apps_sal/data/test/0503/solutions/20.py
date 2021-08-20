(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
lf = {}
rt = {}
for x in a:
    lf[x] = 0
    try:
        rt[x] += 1
    except KeyError:
        rt[x] = 1
prog = 0
for x in a:
    try:
        if x % k == 0:
            rt[x] -= 1
            prog += lf[x // k] * rt[x * k]
    except KeyError:
        pass
    finally:
        lf[x] += 1
print(prog)
