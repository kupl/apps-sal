(n, m) = map(int, input().split())
x = []
y = []
z = []
for i in range(n):
    (X, Y, Z) = map(int, input().split())
    x.append(X)
    y.append(Y)
    z.append(Z)
ppp = []
ppn = []
npp = []
pnp = []
pnn = []
npn = []
nnp = []
nnn = []
for j in range(n):
    ppp.append(x[j] + y[j] + z[j])
    ppn.append(x[j] + y[j] - z[j])
    npp.append(-x[j] + y[j] + z[j])
    pnp.append(x[j] - y[j] + z[j])
    pnn.append(x[j] - y[j] - z[j])
    npn.append(-x[j] + y[j] - z[j])
    nnp.append(-x[j] - y[j] + z[j])
    nnn.append(-(x[j] + y[j] + z[j]))
ppp.sort(reverse=True)
ppn.sort(reverse=True)
npp.sort(reverse=True)
pnp.sort(reverse=True)
pnn.sort(reverse=True)
npn.sort(reverse=True)
nnp.sort(reverse=True)
nnn.sort(reverse=True)
print(max(sum(ppp[:m]), sum(ppn[:m]), sum(npp[:m]), sum(pnp[:m]), sum(pnn[:m]), sum(npn[:m]), sum(nnp[:m]), sum(nnn[:m])))
