(N, K) = map(int, input().split())
lsA = [0] + list(map(int, input().split()))
ls = []
set1 = set()
a = 1
for i in range(N + 1):
    if a in set1:
        loop = ls[ls.index(a):]
        lenloop = len(loop)
        startls = ls[:ls.index(a)]
        break
    ls.append(a)
    set1.add(a)
    a = lsA[a]
if K < len(startls):
    ans = startls[K]
else:
    ans = loop[(K - len(startls)) % lenloop]
print(ans)
