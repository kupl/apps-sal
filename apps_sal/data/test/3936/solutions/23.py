N = int(input())
S = [list(input()) for _ in range(2)]
MOD = 1000000007
i = 0


def define(index):
    if S[0][index] == S[1][index]:
        return 1
    else:
        return 0


if define(i):
    ans = 3
    i += 1
    f_g = 1
else:
    ans = 6
    i += 2
    f_g = 0
while i < N:
    t_g = define(i)
    if f_g == 0 and t_g == 0:
        ans *= 3
        ans %= MOD
    elif not (f_g == 0 and t_g == 1):
        ans *= 2
        ans %= MOD
    if t_g == 1:
        i += 1
    else:
        i += 2
    f_g = t_g
print(ans % MOD)
