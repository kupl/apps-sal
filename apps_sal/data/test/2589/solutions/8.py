for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    a = tuple(map(int, input().split()))
    if sum(a) % x:
        print(n)
    elif any((ai % x for ai in a)):
        non0s = tuple((i for i in range(n) if a[i] % x))
        print(max(max(non0s), n - min(non0s) - 1))
    else:
        print(-1)
