for _ in range(int(input())):
    (n, x, a, b) = map(int, input().split())
    (a, b) = (min(a, b), max(a, b))
    ad = max(1, a - x)
    x -= a - ad
    bd = min(n, b + x)
    print(bd - ad)
