for nt in range(int(input())):
    n, k = list(map(int, input().split()))
    new = list(map(int, input().split()))
    a = []
    for i in range(n):
        if new[i] % k != 0:
            a.append(new[i])
    a.sort()
    n = len(a)
    if n == 0:
        print(0)
        continue
    d = {}
    maxx = 0
    for i in range(n):
        diff = k - (a[i] % k)
        if diff not in d:
            maxx = max(maxx, diff)
            d[diff] = 1
        else:
            maxx = max(maxx, d[diff] * k + diff)
            d[diff] += 1
    print(maxx + 1)
