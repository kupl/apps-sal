from fractions import gcd

t, w, b = map(int, input().split())
mn = min(w, b)
nk = w // gcd(w, b) * b
first = (t  + 1) // nk * mn - 1
e = first + min(mn, (t + 1) % nk)
nd = gcd(e, t)
print(e // nd, "/", t // nd, sep = "")

