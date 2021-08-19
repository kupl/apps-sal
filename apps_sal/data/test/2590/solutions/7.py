for _ in range(int(input())):
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    k = 0
    for i in range(n - 1, -1, -1):
        s += a[i]
        k = n - i
        if s // k < x:
            k -= 1
            break
    print(k)
