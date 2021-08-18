
inln = [int(i) for i in input().split(" ")]
n = inln[0]
m = inln[1]

ln = [int(i) for i in input().split(" ")]
ln = sorted(ln)

cds = []

mds = [0] * m

s = 0

for i in range(0, len(ln)):
    s += (ln[i] + mds[i % m])
    cds.append(s)
    mds[i % m] += ln[i]

print(" ".join([str(i) for i in cds]))
