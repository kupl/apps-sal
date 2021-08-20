for i in range(int(input())):
    (n, k, d) = map(int, input().split())
    a = list(map(int, input().split()))
    mn = 1000000000000
    for i in range(n - d + 1):
        b = set(a[i:i + d])
        if len(b) < mn:
            mn = len(b)
    print(mn)
