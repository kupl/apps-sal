from fractions import gcd
t, w, b = list(map(int, input().split()))
if w > b:
    w, b = b, w
l = w * b // gcd(w, b)
c = t // l
ans = c * w + (min((t + 1) - l * c, w)) - 1
g = gcd(ans, t)
print('{}/{}'.format(ans // g, t // g))

