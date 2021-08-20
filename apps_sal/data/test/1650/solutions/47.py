L = input()
N = len(L)
mod = 10 ** 9 + 7
dpT = [0] * N
dpF = [0] * N
dpT[0] = 1
dpF[0] = 2
for i in range(1, N):
    if L[i] == '1':
        dpT[i] = dpT[i - 1] * 3 + dpF[i - 1] * 1
        dpF[i] = dpF[i - 1] * 2
        dpT[i] %= mod
        dpF[i] %= mod
    else:
        dpT[i] = dpT[i - 1] * 3
        dpF[i] = dpF[i - 1] * 1
        dpT[i] %= mod
        dpF[i] %= mod
print((dpT[-1] + dpF[-1]) % mod)
