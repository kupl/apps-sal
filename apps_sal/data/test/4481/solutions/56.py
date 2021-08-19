n = int(input())
d = {}
t = 0
for i in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
    t = max(t, d[s])
for key in sorted(d):
    if d[key] == t:
        print(key)
