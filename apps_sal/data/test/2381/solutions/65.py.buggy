from functools import reduce

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
Ap = [a for a in A if a > 0]
Am = [a for a in A if a < 0]
mod = 10**9 + 7
if len(Ap) + len(Am) < K:
    print((0))
    return
if len(Ap) + len(Am) == K:
    if 0 in A and len(Am) % 2:
        print((0))
    else:
        ans = reduce(lambda a, b: a * b % mod, Ap + Am, 1)
        print(ans)
    return
Ap.sort(reverse=True)
Am.sort()
if len(Ap) == 0:
    if K % 2:
        if 0 in A:
            ans = 0
        else:
            ans = reduce(lambda a, b: a * b % mod, Am[-K:], 1)
    else:
        ans = reduce(lambda a, b: a * b % mod, Am[:K], 1)
    print(ans)
    return

idx_Am = 0
n = 0
ans = 1
for idx_Ap, ap in enumerate(Ap + [0]):
    while idx_Am < len(Am) and n < K and -Am[idx_Am] > ap:
        ans = ans * Am[idx_Am] % mod
        idx_Am += 1
        n += 1
    if n == K:
        break
    n += 1
    idx_Ap += 1
    ans = ans * ap % mod
    if n == K:
        break
else:
    assert False
if idx_Am % 2 == 0:
    print(ans)
else:
    if idx_Ap == len(Ap) or (idx_Am != len(Am) and idx_Ap > 0 and Am[idx_Am] * Am[idx_Am - 1] > Ap[idx_Ap] * Ap[idx_Ap - 1]):
        ans = ans * Am[idx_Am] * pow(Ap[idx_Ap - 1], mod - 2, mod) % mod
    else:
        ans = ans * Ap[idx_Ap] * pow(Am[idx_Am - 1], mod - 2, mod) % mod
    print(ans)
