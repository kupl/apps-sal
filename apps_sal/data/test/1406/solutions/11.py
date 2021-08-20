def f(t):
    i = -1
    t[i] += 1
    while t[i] > k:
        t[i] = 1
        i -= 1
        t[i] += 1
    return list(map(str, t))


(n, k, d) = map(int, input().split())
if k ** d < n:
    print(-1)
else:
    t = [1] * d
    t[-1] = 0
    s = [f(t) for i in range(n)]
    print('\n'.join([' '.join(t) for t in zip(*s)]))
