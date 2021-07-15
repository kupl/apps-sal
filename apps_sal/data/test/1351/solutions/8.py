inp = lambda cast=int: [cast(x) for x in input().split()]
printf = lambda s='', *args, **kwargs: print(str(s).format(*args), flush=True, **kwargs)

x, y = inp()
for i in range(x, y+1):
    s = str(i)
    if len(s) == len(set(s)):
        print(i)
        return
print(-1)
