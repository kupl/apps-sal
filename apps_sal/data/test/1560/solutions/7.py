n = int(input().strip())
a = list([{'r': 0, 'b': 1}[x] for x in input()])
cb = 0
cr = 0
ccb = 0
ccr = 0
for i, c in enumerate(a):
    cb += (i & 1) & (c ^ 0)
    cr += (~(i & 1)) & (c ^ 1)
    ccb += (i & 1) & (c ^ 1)
    ccr += (~(i & 1)) & (c ^ 0)
ans1 = cb + cr - min(cb, cr)
ans2 = ccb + ccr - min(ccb, ccr)
print(min(ans1, ans2))
