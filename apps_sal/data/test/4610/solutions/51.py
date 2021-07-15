_, k = map(int, input().split())
d = {}
for i in map(int, input().split()):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
d = sorted(d.values(), reverse=True)
print(sum(v for v in d[k:]))
