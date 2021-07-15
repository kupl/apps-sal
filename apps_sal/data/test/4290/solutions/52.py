n,m = map(int,input().split())
if n > 1:
    an = n*(n-1)/2
else:
    an = 0
if m>1:
    am = m*(m-1)/2
else:
    am = 0
print(int(an+am))
