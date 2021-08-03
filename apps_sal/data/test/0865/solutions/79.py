from numpy import*
N, T, *L = int_(open(0).read().split())
d = int_([0] * 6010)
for w, v in sorted(zip(*[iter(L)] * 2)):
    d[w:T + w] = maximum(d[w:T + w], d[:T] + v)
print(max(d))
