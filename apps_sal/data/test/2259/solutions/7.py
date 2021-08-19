MXusl = int
MXuso = input
MXusL = map
MXusr = min
MXusI = print
n = MXusl(MXuso())
a = [1000000.0] * (n + 1)
s = 1
for x in MXusL(MXusl, MXuso().split()):
    l = 0
    r = s
    while r - l > 1:
        m = l + r >> 1
        if a[m] < x:
            l = m
        else:
            r = m
    s += r == s
    a[r] = MXusr(a[r], x)
MXusI(s - 1)
