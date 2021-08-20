S = input()
L = len(S)
mod = 10 ** 9 + 7
dp_c = [0] * L
dp_u = [0] * L
dp_c[0] = 1
dp_u[0] = 2
for i in range(1, L):
    if S[i] == '1':
        dp_c[i] = dp_c[i - 1] * 3 + dp_u[i - 1]
        dp_u[i] = dp_u[i - 1] * 2
    else:
        dp_c[i] = dp_c[i - 1] * 3
        dp_u[i] = dp_u[i - 1] * 1
    dp_c[i] %= mod
    dp_u[i] %= mod
ans = (dp_c[-1] + dp_u[-1]) % mod
print(ans)
