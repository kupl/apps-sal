recipe = input()
(cb, cs, cc) = [recipe.count(x) for x in 'BSC']
(nb, ns, nc) = list(map(int, input().split()))
(pb, ps, pc) = list(map(int, input().split()))
r = int(input())
n_ready = min(nb // cb if cb != 0 else 100, ns // cs if cs != 0 else 100, nc // cc if cc != 0 else 100)
(nnb, nns, nnc) = (nb - n_ready * cb, ns - n_ready * cs, nc - n_ready * cc)


def get_remain_money(n):
    return r - ((pb * (n * cb - nnb) if n * cb - nnb > 0 else 0) + (ps * (n * cs - nns) if n * cs - nns > 0 else 0) + (pc * (n * cc - nnc) if n * cc - nnc > 0 else 0))


lo = 0
hi = max(nb // cb if cb != 0 else 0, ns // cs if cs != 0 else 0, nc // cc if cc != 0 else 0) - n_ready + r // (cb * pb + cs * ps + cc * pc) + 2
while lo < hi - 1:
    mid = (lo + hi) // 2
    if get_remain_money(mid) >= 0:
        lo = mid
    else:
        hi = mid
print(n_ready + lo)
