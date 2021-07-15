n, m = list(map(int, input().split()))
p = tuple(map(int, input().split()))
r = [{i} for i in range(n + 1)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    r[u].add(v)
first = True
nr = set()
res = 0
for i in p[::-1]:
    if first:
        cur = 1
        first = False
    else:
        cur = len(nr)
        for ri in r[i]:
            if ri in nr:
                cur -= 1
    if cur:
        nr.add(i)
    else:
        res += 1
print(res)

