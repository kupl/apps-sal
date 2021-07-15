import sys

n, k = [int(x) for x in (sys.stdin.readline()).split()]

ff, ft = [int(x) for x in (sys.stdin.readline()).split()]

h = 0
if(ft > k):
    h = ff - (ft - k)
else:
    h = ff
    
for i in range(n - 1):
    hh = 0
    f, t = [int(x) for x in (sys.stdin.readline()).split()]
    if(t > k):
        hh = f - (t - k)
    else:
        hh = f
    
    if(hh > h):
        h = hh
    
print(h)
