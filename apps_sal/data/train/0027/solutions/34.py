t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = dict()
    su = 0
    for i in a:
        k = 0
        while i % 2 == 0:
            i = i // 2
            k += 1
        if i not in d:
            d[i] = k
        else:
            d[i] = max(d[i], k)
    for i in list(d.values()):
        su += i
    print(su)
