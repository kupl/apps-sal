n, p,l,r =map(int, input().split())

s1,s2 = 0, 0
l1,l2,r1,r2 = 0, 0 ,0 ,0
p1 = p
if l > 1:
    l1 += abs(p - l)
    l1 += 1
    p1 = l
if r < n:
    r1 += abs(r - p1)
    r1 += 1
s1 = l1+r1
p2 = p
if r < n:
    r2 += abs(r - p2)
    r2 += 1
    p2 = r
if l > 1:
    l2 += abs(p2 - l)
    l2 += 1
s2 = l2+r2
print(min(s1, s2))
