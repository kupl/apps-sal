def case(p, l, r, x):
    l -= 1
    r -= 1
    x -= 1
    a = 0
    t = p[x]
    for i in range(l, r + 1):
        if p[i] < t:
            a += 1
    if a == x - l:
        return "Yes"
    else:
        return "No"


def __starting_point():
    n, m = list(map(int, input().split()))
    p = [int(i) for i in input().split()]
    for i in range(m):
        l, r, x = list(map(int, input().split()))
        print(case(p, l, r, x))


__starting_point()
