K, D, T = list(map(int, input().split()))
ivl = D * ((K + D - 1) // D)
fp = float(K) / float(ivl)
sp = 1.0 - fp
a = 0.0
b = 2.0 * T
for ii in range(300):
    t = 0.5 * (a + b)
    ivls = t // ivl
    cooked = ivls * ivl * (2.0 * fp + sp)
    rt = t - ivls * ivl
    rft = min(fp * ivl, rt)
    rsp = max(0.0, rt - rft)
    cooked += 2.0 * rft + rsp
    if cooked < 2.0 * T:
        a = t
    else:
        b = t
t = 0.5 * (a + b)
print("%.10f" % t)
