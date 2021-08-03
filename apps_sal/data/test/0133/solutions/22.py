N, M = map(int, input().split())
mod = 10**9 + 7

# modを取りながらべき乗する


def power_func(a, n, mod=mod):
    bi = str(format(n, "b"))  # 2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res * res) % mod
        if bi[i] == "1":
            res = (res * a) % mod
    return res


a = power_func(2, M) - 1
if a < 0:
    a += mod
ans = power_func(a, N)
print(ans)
