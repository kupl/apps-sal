(n, vr, vg, vc) = (int(input()), 0, 0, 0)
for x in map(int, input().split()):
    cr = min(vr, vg, vc) + 1
    cg = min(vr, vc) if x & 2 else n
    cc = min(vr, vg) if x & 1 else n
    (vr, vg, vc) = (cr, cg, cc)
print(min(vr, vg, vc))
