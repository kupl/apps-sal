import itertools as it
S = input().strip()
freq = [0 for i in range(10)]
for i in S:
    u = ord(i) - ord('0')
    freq[u] += 1
fac = [1]
for i in range(1, 20):
    fac.append(i * fac[-1])
'\nM={}\ndef F(cur,used):\n    while cur<10 and freq[cur]==0: cur+=1\n    if cur==10:\n        r=fac[sum(used)]\n        for i in used:\n            r//=fac[i]\n        print(used)\n        return 1\n\n    key=(cur,tuple(used))\n    if key in M: return M[key]\n    \n    r=0\n    for i in range(1,freq[cur]):\n        for j in range(\n    return r\n\ntotal=0\nfor i in range(1,10):\n    if freq[i]==0: continue\n    M={}\n    freq[i]-=1\n    used=[0 for j in range(10)]\n    used[i]=1\n    total+=F(0,used)\n    freq[i]+=1\n\nprint(total)\n'
total = 0
for x in it.product(*(list(range(0 if i == 0 else 1, i + 1)) for i in freq)):
    Q = ''.join((str(i) * x[i] for i in range(10)))
    s = sum(x) - 1
    if s < 0:
        continue
    g = 0
    for d in range(1, 10):
        n = fac[s]
        y = list(x)
        y[d] -= 1
        for k in range(0, 10):
            n //= fac[y[k]]
        g += n
    total += g
print(total)
