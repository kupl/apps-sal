import string
n = int(input())
d = dict()
for c in string.ascii_lowercase:
    d[c] = []
for _ in range(n):
    s = input()
    for c in string.ascii_lowercase:
        if s.count(c) != 0:
            d[c].append(s.count(c))
ans = ''
for (k, v) in d.items():
    if len(v) == n:
        ans += k * min(v)
print(ans)
