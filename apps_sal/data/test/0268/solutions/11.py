def bi_search(a, x):
    n = len(a)
    u, l = n, -1
    
    while u-l>1:
        md=(u+l)//2
        
        if x>a[md]:
            l=md
        else:
            u=md
    
    return u 

class Bit():
    # index-1
    def __init__(self, n):
        self.bit = [0] * (n+1) 
        self.n   = n
    
    # sum[1, i]
    def sum_prefix(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i&(-i)
        return s
        
    # sum[l, r]    
    def sum_(self, l, r):
        if l == 1:
            return self.sum_prefix(r)
        return self.sum_prefix(r) - self.sum_prefix(l-1) 
        
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i&(-i)

n, k, d = map(int, input().split())
a = [-1] + list(map(int, input().split()))
a = sorted(a)

B=Bit(n) 
ans=[-1] * n 

for i in range(n+1):
    if i==0:
        continue
        
    pos  = bi_search(a, max(0, a[i]-d)) #pos,   i-k+1..,i-1,i
    
    l, r = pos-1, i-k
    
    if l<=r:
        s=0
        
        if l>=1:
            s+=B.sum_(l, r)
        
        if l==0 or s > 0:
            B.add(i, 1)
            ans[i-1]=1
            
if ans[-1]==1:
    print('YES')
else:
    print('NO')
