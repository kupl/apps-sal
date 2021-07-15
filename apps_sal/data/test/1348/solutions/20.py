n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

d = {}
for idx, x in enumerate(a):
    if x not in d:
        d[x] = [idx]
    else:
        d[x].append(idx)

if 0 not in d or len(d[0]) != 1:
    print(-1)
    import sys; return

res = []

for x in range(1, max(d.keys())+1):
    if x not in d or len(d[x]) > len(d[x-1])*(k if x-1 is 0 else k-1):
        print(-1)
        import sys; return
    t = d[x][:]
    p = d[x-1][:]
    z = (0 if x-1 is 0 else 1)
    while(t):
        res.append((p[-1]+1, t[-1]+1))
        del t[-1]
        z += 1
        if z == k:
            z = 1
            del p[-1]
        
print(len(res))
for x, y in res:
    print(x, y)
