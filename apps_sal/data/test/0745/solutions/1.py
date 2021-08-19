MOD = 998244353
list_size = 200001
f_list = [1] * list_size
f_r_list = [1] * list_size
for i in range(list_size - 1):
    f_list[i + 1] = int(f_list[i] * (i + 2) % MOD)
f_r_list[-1] = pow(f_list[-1], MOD - 2, MOD)
for i in range(2, list_size + 1):
    f_r_list[-i] = int(f_r_list[-i + 1] * (list_size + 2 - i) % MOD)


def comb(n, r):
    if n < r:
        return 0
    elif n == 0 or r == 0 or n == r:
        return 1
    else:
        return f_list[n - 1] * f_r_list[n - r - 1] % MOD * f_r_list[r - 1] % MOD


(n, k) = list(map(int, input().split()))
if k >= n:
    print(0)
elif k == 0:
    print(f_list[n - 1])
else:
    ans = 0
    m = n - k
    for i in range(1, m + 1):
        ans += (-1) ** ((m - i) % 2) * pow(i, n, MOD) * comb(m, i)
        ans %= MOD
    ans *= f_r_list[m - 1] * f_list[n - 1] * f_r_list[k - 1]
    ans *= 2
    print(ans % MOD)
