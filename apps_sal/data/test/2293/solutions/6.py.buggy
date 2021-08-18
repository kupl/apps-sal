def inp(cast=int): return list(map(cast, input().split()))


printf = lambda s='', *args, **kwargs: print(str(s).format(*args), flush=True, **kwargs)
m, n = inp()
A = []
for _ in range(m):
    l = inp()
    A.append(set(l[1:]))
for i in range(m):
    for j in range(m):
        if i == j:
            continue
        if not A[i].intersection(A[j]):
            print('impossible')
            return
print('possible')
