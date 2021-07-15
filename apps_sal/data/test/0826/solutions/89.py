n = int(input())
l, r =0, 1000000000000000000
while r - l > 1 :
    m = (l+r)//2
    tmps = m*(m+1)//2
    if tmps <= n+1: l = m
    else: r = m
print(n-l+1)
