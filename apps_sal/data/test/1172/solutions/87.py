s = input()
n_a = [0]
n_l = [0]
n_c = [0]
n_r = [0]
mod = 10 ** 9 + 7
n = len(s)
pow3 = [1]
for i in range(n):
    pow3.append(pow3[-1] * 3 % mod)
for i in range(n):
    if s[i] == 'A':
        n_a.append(n_a[-1] + 1)
    else:
        n_a.append(n_a[-1])
    if s[i] == '?':
        n_l.append(n_l[-1] + 1)
    else:
        n_l.append(n_l[-1])
    if s[-i - 1] == 'C':
        n_c.append(n_c[-1] + 1)
    else:
        n_c.append(n_c[-1])
    if s[-i - 1] == '?':
        n_r.append(n_r[-1] + 1)
    else:
        n_r.append(n_r[-1])
ans = 0
for i in range(1, n - 1):
    if s[i] in ['B', '?']:
        ans += n_a[i] * n_c[n - 1 - i] * pow3[n_l[i]] * pow3[n_r[n - 1 - i]] % mod
        ans %= mod
        ans += n_l[i] * n_c[n - 1 - i] * pow3[n_l[i] - 1] * pow3[n_r[n - 1 - i]] % mod
        ans %= mod
        ans += n_a[i] * n_r[n - 1 - i] * pow3[n_l[i]] * pow3[n_r[n - 1 - i] - 1] % mod
        ans %= mod
        ans += n_l[i] * n_r[n - 1 - i] * pow3[n_l[i] - 1] * pow3[n_r[n - 1 - i] - 1] % mod
        ans %= mod
print(ans)
