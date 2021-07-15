from collections import Counter
s = Counter(input())
t = Counter(input())
r1 = 0
for k in s:
    d = min(s[k], t[k])
    s[k] -= d
    t[k] -= d
    r1 += d
r2 = 0
for k in s:
    if k.islower():
        l = k.upper()
    else:
        l = k.lower()
    d = min(s[k], t[l])
    r2 += d
    s[k] -= d
    t[l] -= d
print(r1, r2)
