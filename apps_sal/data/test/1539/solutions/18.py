def f(): return list(map(int, input().split()))


n, p, m, s = input(), {}, 0, sorted(zip(f(), f()), key=lambda q: -q[1])
for L, d in s:
    k, D = p.get(L, (-1, 0))
    p[L] = (k + 1, D + d)
for L, (k, D) in list(p.items()):
    if k:
        for l, d in s:
            if l < L:
                D += d
                k -= 1
                if k == 0:
                    break
    m = max(D, m)
print(sum(d for l, d in s) - m)
