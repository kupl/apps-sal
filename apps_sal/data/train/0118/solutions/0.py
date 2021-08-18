__MULTITEST = True


def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    group = 0
    ptr = n - 1
    members = 0

    currentMin = int(1e10)
    while ptr > -1:
        currentMin = min(currentMin, a[ptr])
        members += 1

        if currentMin * members >= x:
            group += 1
            members = 0
            currentMin = int(1e10)

        ptr -= 1

    print(group)


def __starting_point():
    t = (int(input()) if __MULTITEST else 1)
    for tt in range(t):
        solve()


__starting_point()
