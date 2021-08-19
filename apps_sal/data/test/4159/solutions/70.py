(a, b, n) = map(int, input().split())
if a >= n:
    a -= n
    print(a, b)
elif a < n:
    n -= a
    if n >= b:
        print(0, 0)
    else:
        print(0, b - n)
