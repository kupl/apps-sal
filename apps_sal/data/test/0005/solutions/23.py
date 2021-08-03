
n, pos, l, r = [int(x) for x in input().split(' ')]
ans = 0
ra = abs(pos - r)
la = abs(pos - l)
if l == 1:
    if r == n:
        print(0)
    else:
        print(ra + 1)
else:
    if r == n:
        print(la + 1)
    else:
        if la < ra:
            print(r - l + 2 + la)
        else:
            print(r - l + 2 + ra)
