MOD = 998244353

n, k = map(int, input().split())
a = list(map(int, input().split()))

ch = []
lt = None
for beg in (0, 1):
    for i in range(beg, n, 2):
        if a[i] == -1:
            if lt is None:
                lt = -1 if i - 2 < 0 else a[i - 2]
                sz = 0
            sz += 1
            if i + 2 >= n:
                ch.append((lt, -1, sz))
                lt = None
            elif a[i + 2] != -1:
                ch.append((lt, a[i + 2], sz))
                lt = None

ans = int(all(a[i] != a[i + 2] for i in range(n - 2) if a[i] != -1))
for lt, rt, sz in ch:
    if sz == 1:
        cur = k if lt == -1 and rt == -1 else k - 1 if lt == -1 or rt == -1 or lt == rt else k - 2
    else:
        eq, neq = 1 if lt == -1 else 0, 1
        for _ in range(sz - 1):
            eq, neq = neq * (k - 1) % MOD, (neq * (k - 2) + eq) % MOD
        cur = neq * (k - 1) + eq if rt == -1 else neq * (k - 1) if lt == rt else neq * (k - 2) + eq
    ans = ans * cur % MOD
print(ans)
