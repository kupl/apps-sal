for gfhua in range(int(input())):
    n, m, k = list(map(int, input().split()))
    mk = min(m, n // k)
    m -= mk
    if m == 0:
        print(mk)
    else:
        print(mk - (m + k - 2) // (k - 1))
