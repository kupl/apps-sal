n, k, *a = map(int, open(0).read().split())
s = r = 0
for x in sorted(a)[::-1]:
    if s + x < k:
        s += x
        r += 1
    else:
        r = 0
print(r)

"""
Σ_[i=m,n]>kのときa(m)以降は凡て必要
(∵ a(i)が必要->a(i+1)が必要)
k-=Σ_[i=m+1,n]として操作を続ける
Σ_[i=1,r]<kとなったときa(r)までが不必要
"""
