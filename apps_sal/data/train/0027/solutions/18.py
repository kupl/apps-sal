t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    d = {}
    for el1 in m:
        el = el1
        c = 0
        while el % 2 == 0:
            el //= 2
            c += 1
        if el in list(d.keys()):
            d[el] = max(d[el], c)
        else:
            d[el] = c
    s = 0
    for el in d:
        s += d[el]
    ans.append(s)
for el in ans:
    print(el)
