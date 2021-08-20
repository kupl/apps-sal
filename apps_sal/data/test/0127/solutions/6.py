(n, f) = list(map(int, input().split()))
ans = 0
L = []
for _ in range(n):
    (p, c) = list(map(int, input().split()))
    s = min(p, c)
    sf = min(2 * p, c)
    ans += s
    L.append(sf - s)
L.sort(reverse=True)
ans += sum([x for x in L[:f] if x > 0])
print(ans)
