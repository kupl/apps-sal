n = int(input())
s = list(input() for _ in range(n))
d = {}
for i in range(n):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

m = max(d.values())
l = []
for i in d:
    if d[i] == m:
        l.append(i)
for i in sorted(l):
    print(i)
