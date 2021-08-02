n, k = map(int, input().split())
a = [int(x) for x in input().split()]
s = sum(a)

candidates = set()
for i in range(1, int(s**0.5) + 1):
    if s % i == 0:
        candidates.add(i)
        candidates.add(s // i)

ans = 0
for cdd in candidates:
    div_cdd = [0] * n
    for i in range(n):
        div_cdd[i] = a[i] % cdd
    div_cdd = sorted(div_cdd)
    pstv, ngtv = 0, -sum(div_cdd)
    # calc need
    if pstv == -ngtv:
        ans = max(ans, cdd)
        continue
    for i in range(n):
        pstv += cdd - div_cdd[-1 - i]
        ngtv += div_cdd[-1 - i]
        if pstv == -ngtv: break
    ans = max(ans, cdd) if pstv <= k else ans

print(ans)
