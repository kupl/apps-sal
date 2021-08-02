
MOD = 2019
L, R = list(map(int, input().split()))
mod_l = L % MOD
mod_r = R % MOD

if R - L >= 2019:
    print("0")
else:
    ans = 2018
    for i in range(mod_l, mod_r):
        for j in range(i + 1, mod_r + 1):
            _ans = (i * j) % MOD
            if ans > _ans:
                ans = _ans
    print(ans)
