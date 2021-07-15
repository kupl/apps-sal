n, k = map(int, input().split())
if n < 3 * k: print(-1)
else:
    d = n // k
    p = [min(1 + i // d, k) for i in range(n)]
    
    for i in range(d, n, 2 * d):
        p[i], p[i - 1] = p[i - 1], p[i]
    if k > 2: p[0], p[-1] = p[-1], p[0]
    print(' '.join(str(i) for i in p))
