n = int(input())
s = list((input() for _ in range(n)))
d = {}
for i in range(n):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1
m = max(d.values())
for s in sorted((k for k in d if d[k] == m)):
    print(s)
