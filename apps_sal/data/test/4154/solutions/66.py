def resolve():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        nl, nr = map(int, input().split())
        l = max(l, nl)
        r = min(r, nr)
    print(max(r - l + 1, 0))


resolve()
