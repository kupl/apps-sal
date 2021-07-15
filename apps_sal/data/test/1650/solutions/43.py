L = list(input())
N = len(L)
if '0' not in L:
    L = ['1'] + ['0']*N
    N += 1
else:
    for i in range(N):
        t = L[N-i-1]
        if t == '0':
            L[N-i-1] = '1'
            break
        else:
            L[N-i-1] = '0'
res = 0
MOD = 10**9+7
buff = 1
for d, char in enumerate(L):
    if char == '1':
        res = (res + buff * pow(3, N-1-d, MOD))%MOD
        buff = (2 * buff) % MOD
print(res)


