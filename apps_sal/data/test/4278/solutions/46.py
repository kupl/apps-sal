import collections
from scipy.special import comb
n = int(input())
aa = []
for i in range(n):
    s = sorted(input())
    s = [''.join(s)]
    aa.append(*s)
cc = collections.Counter(aa)
c = [c[1] for c in cc.items() if c[1] > 1]
ans = 0
for i in range(len(c)):
    ans += comb(c[i], 2, exact=True)
print(int(ans))
