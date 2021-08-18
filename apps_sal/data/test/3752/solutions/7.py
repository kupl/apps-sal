[k, d, t] = input().split()
k = int(k)
d = int(d)
t = int(t)

if k % d == 0:
    d = k
if k > d and k % d != 0:
    d = (k // d + 1) * d


p1 = 1.0 * k / t
p2 = 0.5 * (d - k) / t
p = p1 + p2
s = 1.0 / p
c = int(s)
z = 1.0 - p * c
if z < p1:
    ans = c * d + 1.0 * z * t
else:
    ans = c * d + k
    z = z - p1
    ans += 2.0 * z * t
template = '{:.' + str(10) + 'f}'
print(template.format(ans))
