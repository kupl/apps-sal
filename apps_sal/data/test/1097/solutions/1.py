def __starting_point():
    (n, t, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0 for _ in range(t)]
    b[t - 1] = a[t - 1]
    maxk = a[t - 1]
    for i in range(t - 2, -1, -1):
        b[i] = b[i + 1]
        if a[i + 1] < a[i]:
            b[i] += a[i] - a[i + 1]
        maxk += a[i] - 1
    if b[0] > k or maxk < k:
        print(-1)
    else:
        print(n)
        curr = 2
        for _ in range(a[0]):
            print(1, curr)
            curr += 1
        for lvl in range(t - 1):
            childless = min(a[lvl] - 1, k - b[lvl + 1])
            parent = curr - 1
            for _ in range(a[lvl] - childless):
                print(parent, curr)
                curr += 1
                parent -= 1
            parent += 1
            for _ in range(a[lvl + 1] - (a[lvl] - childless)):
                print(parent, curr)
                curr += 1
            k -= childless


'\n\t\t\tparent = curr-1\n\t\t\tchildren = min(a[lvl+1], k-b[lvl]+1)\n\t\t\tprint("#DEBUG", lvl, children)\n\t\t\tfor _ in range(children):\n\t\t\t\tprint(parent, curr)\n\t\t\t\tcurr += 1\n\t\t\tparent -= 1\n\t\t\tk -= a[lvl]+1\n\t\t\tfor _ in range(a[lvl]-children):\n\t\t\t\tprint(parent, curr)\n\t\t\t\tparent -= 1\n\t\t\t\tcurr += 1\n\t\t\t\tk += 1\n'
__starting_point()
