for _ in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    c = 0
    b = [0] * n
    for i in range(n):
        if 2 * a[i] == k:
            b[i] = c
            c = 1 - c
        elif a[i] in s:
            b[i] = 1
        else:
            s.add(k - a[i])
    print(*b)
