n = int(input())
s_p = [list(map(str, input().split())) for i in range(n)]

d = {}
for i, v in enumerate(s_p):
    s = v[0]
    p = v[1]
    if s not in d.keys():
        d[s] = [(i, p)]
    else:
        d[s] = sorted(d[s] + [(i, p)], key=lambda x: int(x[1]), reverse=True)

for key in sorted(d.keys()):
    for i, j in d[key]:
        print(i + 1)
