d = dict()
for _ in range(int(input())):
    s = input()
    d[s] = d.get(s, 0) + 1
m = max(d.values())
i = [k for k, v in d.items()if v == m]
for v in sorted(i):
    print(v)
