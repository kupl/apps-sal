import math

h, w, a, b = list(map(int, input().split()))

mod = pow(10, 9) + 7


def divmod(num, mod=10**9 + 7):
    return pow(num, mod - 2, mod)


def comb(a, b):
    p = fact[a - b] * fact[b] % mod
    return fact[a] * divmod(p) % mod


fact = [1]
for i in range(1, h + w):
    fact.append(i * fact[i - 1] % mod)

ans = 0
for j in range(h - a):
    tmp = comb(b - 1 + j, j) * comb(w + h - b - 2 - j, w - b - 1) % mod
    ans += tmp
    ans = ans % mod
print((int(ans)))

'''
単純なh*wのマス目だった場合
con = [[0]*w]*h
for i in range(h):
    con[i][0] = 1
for j in range(w):
    con[0][j] = 1

for k in range(1,h):
    for l in range(1,w):
        con[k][l] = con[k-1][l] + con[k][l-1]

print(con[h-1][w-1])
'''

'''
全量を計算するやり方
H*Wがデカすぎると時間というよりもメモリエラー
print('initialize')
con = [[0 for i in range(w)] for j in range(h)]
print('initialize finished')


for i in range(h-a):
    con[i][0] = 1
for j in range(w):
    con[0][j] = 1

for k in range(1,h-a):
    for l in range(1,b+1):
        con[k][l] = con[k-1][l] + con[k][l-1]

for m in range(1,h):
    for n in range(b,w):
        con[m][n] = con[m-1][n] + con[m][n-1]

print(con[h-1][w-1])
'''
