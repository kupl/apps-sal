rr = lambda: map(int, input().split())
_, d, res, he = input(), {}, 0, list(zip(rr(), rr()))
for h, e in he:
    f, x = d.get(h, (-1, 0))
    d[h] = (f + 1, x + e)
he.sort(key = lambda x: x[1], reverse=True)
for h, (f, x) in d.items():
    if not f:
    	res = max(x, res)
    	continue
    for h1, e in he:
        if h1 < h:
            x += e
            f -= 1
            if not f: break
    res = max(x, res)
print(sum(e for h, e in he) - res)
