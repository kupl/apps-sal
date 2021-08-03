for nt in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    if s % x != 0:
        print(n)
        continue
    f, s = -1, -1
    for i in range(n):
        if a[i] % x != 0:
            f = i
            break
    for i in range(n - 1, -1, -1):
        if a[i] % x != 0:
            s = i
            break
    if f == -1:
        print(-1)
        continue
    print(n - (min(f + 1, n - s)))
