def binsearch(a, x, k):
    l = 0
    r = k
    while l < r - 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    return l


n = int(input())
k = -1
a = [0] * n
for i in input().split():
    x = int(i)
    if k == -1:
        k += 1
        a[k] = x
    else:
        if x >= a[k]:
            k += 1
            a[k] = x
        else:
            k1 = k
            k = binsearch(a, x, k + 1)
            if a[k] <= x:
                k += 1
            a[k] = a[k1]
print(k + 1)
