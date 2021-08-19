(n, k) = map(int, input().split())
a = [int(x) for x in input().split()]
s = sum(a)
candidates = set()
for i in range(1, int(s ** 0.5) + 1):
    if s % i == 0:
        candidates.add(i)
        candidates.add(s // i)
ans = 0
for cdd in candidates:
    div_cdd = [0] * n
    for i in range(n):
        div_cdd[i] = a[i] % cdd
    div_cdd = sorted(div_cdd)
    idx = n - sum(div_cdd) // cdd
    need = 0
    for i in range(idx):
        need += div_cdd[i]
    ans = max(ans, cdd) if need <= k else ans
print(ans)
