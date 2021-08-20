def foo():
    (n, m, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    if m <= k:
        print(0)
        return
    i = 0
    for x in a:
        k += x - 1
        i += 1
        if m <= k:
            print(i)
            return
    print(-1)


foo()
