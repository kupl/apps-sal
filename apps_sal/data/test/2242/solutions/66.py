from collections import Counter
S = input()
S = S + '0'
mod = 2019
p = [-1] * len(S)
r = 0
d = 1
for (i, s) in enumerate(S[::-1]):
    t = int(s) % mod
    r += t * d
    r %= mod
    d = d * 10 % mod
    p[i] = r
ans = 0
c = Counter(p)
for (k, n) in c.most_common():
    if n > 1:
        ans += n * (n - 1) // 2
    else:
        break
print(ans)
