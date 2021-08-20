n = int(input())
a = list(map(int, input().split()))
q = int(input())
d = dict()
for i in range(n):
    if a[i] not in d.keys():
        d[a[i]] = 1
    else:
        d[a[i]] += 1
s = sum([k * v for (k, v) in d.items()])
for i in range(q):
    (b, c) = list(map(int, input().split()))
    if b in d.keys():
        s += (c - b) * d[b]
        if c in d.keys():
            d[c] += d[b]
            d[b] = 0
        else:
            d[c] = d[b]
            d[b] = 0
    print(s)
