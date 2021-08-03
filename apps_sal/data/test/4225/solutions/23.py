a, b, c, k = map(int, input().split())
if k <= a:
    print(k)
else:
    m = min(k, a)
    k -= a

    if k <= b:
        print(a)
    else:
        n = min(k, b)
        k -= b
        l = k
        print(1 * m + (-1) * l)
