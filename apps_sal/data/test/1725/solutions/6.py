from itertools import chain
n, m, d = map(int, input().split())
a = [map(int, input().split()) for i in range(n)]
p = sorted(chain.from_iterable(a))
e = set()
ans = 0
for i in p:
    e.add(i % d)
if len(e) > 1:
    print(-1)
    return
else:
    if len(p) % 2 == 0:
        med = p[(len(p) // 2) - 1]
        for i in p:
            ans += abs(i - med)
        print(ans // d)
    else:
        med = p[(len(p) // 2)]
        for i in p:
            ans += abs(i - med)
        print(ans // d)
