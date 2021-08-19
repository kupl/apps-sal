(n, v, ps, pp) = (int(input()), 0, 0, 0)
for l in sorted(map(int, input().split()), reverse=True):
    if ps == 0 or ps > l + 1:
        ps = l
    elif pp == 0:
        (pp, ps) = (l, 0)
    else:
        (v, pp, ps) = (v + pp * l, 0, 0)
print(v)
