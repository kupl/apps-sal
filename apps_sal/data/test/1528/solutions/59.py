def solve():
    (n, x) = list(map(int, input().split()))
    l = [1]
    nu = [1]
    for i in range(n):
        l.append(l[-1] * 2 + 3)
        nu.append(nu[-1] * 2 + 1)

    def chris(a, b):
        if a == 0:
            return b
        elif b <= a:
            return 0
        hl = l[a]
        if b >= hl - a:
            return nu[a]
        elif hl // 2 + 1 <= b:
            return nu[a - 1] + 1 + chris(a - 1, b - (hl // 2 + 1))
        return chris(a - 1, b - 1)
    print(chris(n, x))


solve()
