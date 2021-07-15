t = int(input())

while t:
    t -= 1
    n = int(input())
    s = list(input())
    a = [(-1 if s[i] == 'L' else (1 if s[i] == 'R' else 0)) for i in range(n)]
    b = [(-1 if s[i] == 'D' else (1 if s[i] == 'U' else 0)) for i in range(n)]
    suma = [a[0] for _ in range(n)]
    sumb = [b[0] for _ in range(n)]
    d = dict()
    d[(0, 0)] = -1
    for i in range(1, n):
        suma[i] = suma[i - 1] + a[i]
        sumb[i] = sumb[i - 1] + b[i]
    res = n + 1
    _res = -1
    for i in range(n):
        #print(suma[i], sumb[i])
        if (suma[i], sumb[i]) in d.keys():
            if res > i - d[(suma[i], sumb[i])]:
                res = i - d[(suma[i], sumb[i])]
                _res = (d[(suma[i], sumb[i])], i)
        d[(suma[i], sumb[i])] = i
    if (_res == -1):
        print(_res)
    else:
        print(_res[0] + 2, _res[1] + 1) 
