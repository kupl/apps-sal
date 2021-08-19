for f in range(int(input())):
    (k, n, a, b) = [int(i) for i in input().split()]
    k -= 1
    q = k - n * b
    if q < 0:
        print(-1)
    else:
        print(min(q // (a - b), n))
