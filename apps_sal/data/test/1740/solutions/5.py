n = int(input())
d = {}
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    if (a not in list(d.keys())) and (b not in list(d.keys())):
        d[a] = [a, b]
        d[b] = d[a]
    elif (a in list(d.keys())) and (b not in list(d.keys())):
        d[a] += [b]
        d[b] = d[a]
    elif (a not in list(d.keys())) and (b in list(d.keys())):
        d[b] += [a]
        d[a] = d[b]
    else:
        d[a] += d[b]
        for j in d[b]:
            d[j] = d[a]
print(*d[1])
