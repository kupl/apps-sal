import itertools
s = input()
l = [*itertools.accumulate(s)]
o = []
for b in range(1 << len(s) - 1):
    q = []
    p = 0
    for i in range(len(s) - 1):
        if b & 1 << i:
            q += (int(l[i][p:]),)
            p = i + 1
    c = l[-1][p:]
    c = c if c else 0
    q += (int(c),)
    o += (sum(q),)
print(sum(o))
