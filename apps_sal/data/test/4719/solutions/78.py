n = int(input())
d = {}
s = input()
for c in set(s):
    d[c] = s.count(c)
for _ in range(n - 1):
    s = input()
    for c in d.keys():
        d[c] = min(d[c], s.count(c))
d_sorted = sorted(d.items(), key=lambda x: x[0])
ans = ''
for item in d_sorted:
    ans += item[0] * item[1]
print(ans)
