def main():
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i + 1)
        else:
            d[a[i]] = [i + 1]
    count = 0
    ans = []
    a.sort()
    s = 0
    count = 0
    b = []
    i = 0
    while s + a[i] <= k:
        s += a[i]
        i += 1
        if i == n:
            break
    if i == n:
        count = n
        print(n)
    else:
        print(i)
    for x in range(i):
        print(d[a[x]][0], end=' ')
        d[a[x]].remove(d[a[x]][0])


def __starting_point():
    main()


__starting_point()
