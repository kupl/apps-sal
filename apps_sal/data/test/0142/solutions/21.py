n, l = map(int, input().split())
c = list(map(int, input().split()))

v = []
for i in range(n):
    v.append(2**i)
from math import ceil
def sl(n,l,c, bl):
    #print(n, l, c, bl)
    s = []
    for i in range(n):
        if i not in bl:
            s.append((v[i], v[i]/c[i], c[i], i))
    sm = min(s, key=lambda x: -x[1])
    ct = ceil(l / sm[0])
    if sm[0] == 1:
        return ct*sm[2]
    ans = (ct-1)*sm[2]
    ans1 = min(sm[2], sl(n, l-(ct-1)*sm[0], c, bl + [sm[3]]))
    return ans + ans1
print(sl(n, l, c, []))
