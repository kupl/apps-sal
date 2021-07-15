class F:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]
    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1
    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x
    def findkth(self, k):
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1
import sys
z=sys.stdin.readline
y=lambda:map(int,z().split())
n,q=y()
v=F([0]*(n-2))
h=F([0]*(n-2))
w=j=n-2
s=0
for _ in range(q):
    a,b=y()
    if a<2:
        if b-2<w:h.update(n-2-j,w-b+2);w=b-2
        s+=n-2-v.query(n-b)
    else:
        if b-2<j:v.update(n-2-w,j-b+2);j=b-2
        s+=n-2-h.query(n-b)
print((n-2)*(n-2)-s)
