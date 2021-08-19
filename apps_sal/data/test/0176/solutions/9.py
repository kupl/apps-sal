(k, l, r) = map(int, input().split())
p = l // k
if l % k > 0:
    p += 1
l = p * k
o = (r - l) // k + 1
if l > r:
    o = 0
print(o)
