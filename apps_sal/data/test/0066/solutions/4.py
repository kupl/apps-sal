from fractions import gcd
(t, w, b) = map(int, input().split())
nok = w * b // gcd(w, b)
ans = t // nok * min(w, b) + min(w - 1, b - 1, t % nok)
(ans, t) = (ans // gcd(ans, t), t // gcd(ans, t))
print(ans, t, sep='/')
