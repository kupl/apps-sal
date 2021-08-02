n, pos, l, r = [int(v) for v in input().split()]

needleft = l > 1
needright = r < n
if needleft:
    if needright:
        dl = abs(pos - l)
        dr = abs(pos - r)
        print(min(dl, dr) + 1 + r - l + 1)
    else:
        print(abs(pos - l) + 1)
else:
    if needright:
        print(abs(pos - r) + 1)
    else:
        print(0)
