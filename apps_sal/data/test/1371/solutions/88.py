n = int(input())
mod = 10**9 + 7

per = [1] * (n + 1)
for i in range(1, n + 1):
    per[i] = per[i - 1] * i
    per[i] %= mod

inv = [1] * (n + 1)
inv[-1] = pow(per[-1], mod - 2, mod)
for j in range(2, n + 2):
    inv[-j] = inv[-j + 1] * (n - j + 2)
    inv[-j] %= mod


def C(n, k):
    cmb = per[n] * inv[k] * inv[n - k]
    cmb %= mod
    return cmb


total = 0
for k in range(1, n + 1):
    if n < 3 * k:
        break
    total += C(n - 2 * k - 1, k - 1)
    total %= mod

print(total)
