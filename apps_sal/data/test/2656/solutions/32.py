k = int(input())
s = input()
len_s = len(s)
MOD = 1000000007
x_i = pow(26, k, MOD)
r = 25 * pow(26, -1, MOD) % MOD
comb_i = 1
a = 0
for i in range(k + 1):
    a += comb_i * x_i % MOD
    a %= MOD
    x_i = x_i * r % MOD
    comb_i = comb_i * (len_s + i) * pow(i + 1, -1, MOD) % MOD
print(a)
