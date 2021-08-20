def main():
    (n, d, k) = list(map(int, input().split()))
    (r, odd) = divmod(d, 2)
    k -= 1
    cap = d + 1 if k == 1 else 1
    if k > 1:
        cap = 2 * (k ** (r + 1) - 1) // (k - 1) if odd else 1 + (k + 1) * (k ** r - 1) // (k - 1)
    if n == 1 or k < 1 < n - 1 or (k == 1 and d != n - 1) or (d >= n) or (k > 1 and (not d < n <= cap)):
        print('NO')
        return

    def dfs(parent, depth):
        stack = []
        for _ in range(k - 1):
            child = rest.pop()
            res.append('%s %s' % (parent, child))
            if depth:
                stack.append((child, depth))
        while stack:
            (parent, depth) = stack.pop()
            depth -= 1
            for _ in range(k):
                child = rest.pop()
                res.append('%s %s' % (parent, child))
                if depth:
                    stack.append((child, depth))
    res = ['YES']
    for pc in enumerate(list(range(2, d + 2)), 1):
        res.append('%d %d' % pc)
    rest = list(range(n, d + 1, -1))
    try:
        for p in range(r + 1, r + odd + 2):
            dfs(p, r - 1)
        for (de, p, q) in zip(list(range(r - 2, -1, -1)), list(range(r, 1, -1)), list(range(r + odd + 2, d + 1))):
            dfs(p, de)
            dfs(q, de)
    except IndexError:
        pass
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
