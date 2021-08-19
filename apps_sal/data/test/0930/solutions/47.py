(n, k) = map(int, input().split())
mod = 10 ** 9 + 7
list_size = 4 * 10 ** 5 + 1
f_list = [1] * list_size
f_r_list = [1] * list_size
for i in range(list_size - 1):
    f_list[i + 1] = f_list[i] * (i + 1) % mod
f_r_list[-1] = pow(f_list[-1], mod - 2, mod)
for i in range(list_size - 2, -1, -1):
    f_r_list[i] = f_r_list[i + 1] * (i + 1) % mod


def comb(n, r, mod):
    if n < r or r < 0:
        return 0
    elif n == 0 or r == 0 or n == r:
        return 1
    else:
        return f_list[n] * f_r_list[n - r] * f_r_list[r] % mod


if k < n - 1:
    ans = 0
    for i in range(k + 1):
        ans += comb(n - 1, i, mod) * comb(n, i, mod) % mod
    print(ans % mod)
else:
    print(comb(2 * n - 1, n, mod) % mod)
