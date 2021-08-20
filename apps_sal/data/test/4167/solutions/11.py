(n, k) = map(int, input().split())
ans = 0
if k > 2 * n:
    print(ans)
else:
    r = k
    for i in range(1, k):
        if 2 * i % k == 0:
            r = i
    amari = set()
    for i in range(1, (n - r) // r + 1 + 1):
        if r * i % k in amari:
            continue
        else:
            amari.add(r * i % k)
            q = (n - r * i) // k + 1
            ans += q ** 3
    print(ans)
