for i in range(int(input())):
    n, u, a, b = map(int, input().split())
    if n % 3:
        print('no')
    else:
        if a > b:
            a, b = b, a
        p, q = a + b, 2 * b - a
        s, r, v = p + a, p + b, n - u
        t = [(p, q), (q, p), (s, r), (r, s)]
        print('no' if all(x > u or (x - u) % 3 or y > v or (y - v) % 3 for x, y in t) else 'yes')
