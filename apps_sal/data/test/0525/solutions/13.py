def inp(cast=int):
    return [cast(x) for x in input().split()]


printf = lambda s='', *args, **kwargs: print(str(s).format(*args), flush=True, **kwargs)
(t,) = inp()
for _ in range(t):
    (n,) = inp()
    print(n if len(set(inp())) == 1 else 1)
