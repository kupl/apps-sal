t = int(input(''))
for _ in range(t):
    n = int(input(''))
    a = list(map(int, input('').split(' ')))
    d = {}
    for i in range(n):
        if(a[i] not in d):
            d[a[i]] = 0
        d[a[i]] = d[a[i]] + 1
    mx = 0
    l = len(d)
    for k in d:
        if(min(d[k], l - 1) > mx):
            mx = min(d[k], l - 1)
        if(min(d[k] - 1, l) > mx):
            mx = min(d[k] - 1, l)
    print(mx)
