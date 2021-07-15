def f(a, l):
    m = a[l]
    mi = l
    for i in range(l, len(a)):
        if a[i] < m:
            m = a[i]
            mi = i

    for i in range(mi, l, -1):
        a[i] = a[i - 1]
    a[l] = m
    return mi if mi != l else mi + 1


for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    mi = 0
    while mi < n:
        mi = f(a, mi)
    print(*a)

