t = int(input())
for _ in range(t):
    n = int(input())
    skills = map(int, input().split())
    d = {}
    for s in skills:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    m = 0
    for k in d.keys():
        m = max(m, max(min(d[k], len(d) - 1), min(d[k] - 1, len(d))))
    print(m)
