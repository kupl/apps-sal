tests = int(input())
for test in range(tests):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in range(n):
        s = 0
        while a[i] % 2 == 0:
            a[i] //= 2
            s += 1
        if a[i] in list(d.keys()):
            d[a[i]] = max(s, d[a[i]])
        else:
            d[a[i]] = s
    s = 0
    for i in list(d.keys()):
        s += d[i]
    print(s)
