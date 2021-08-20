from itertools import accumulate
vowels = set('AIUEOY')
s = input()
n = len(s)
vs = list(accumulate((0 if i == 0 else 1 / i for i in range(n + 1))))
r = 0
v = 0
for i in range(n):
    v += vs[n - i] - vs[i]
    if s[i] in vowels:
        r += v
print(r)
