q = int(input())
for rwre in range(q):
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ll = l.copy()
    p = list(map(int, input().split()))
    p.sort()
    i = 0
    while i < 100000:
        i += 1
        if l[p[i % m] - 1] > l[p[i % m]]:
            a = l[p[i % m] - 1]
            b = l[p[i % m]]
            l[p[i % m] - 1] = b
            l[p[i % m]] = a
    ll.sort()
    if l == ll:
        print("YES")
    else:
        print("NO")
