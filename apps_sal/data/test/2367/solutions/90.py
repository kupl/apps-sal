import math

h, w, a, b = list(map(int, input().split()))

# divmod
mod = pow(10, 9) + 7


def divmod(num, mod=10**9 + 7):
    return pow(num, mod - 2, mod)

# combination


def comb(a, b):
    p = fact[a - b] * fact[b] % mod
    return fact[a] * divmod(p) % mod


fact = [1]
for i in range(1, h + w):
    fact.append(i * fact[i - 1] % mod)
# print(fact)

ans = 0
for j in range(h - a):
    tmp = comb(b - 1 + j, j) * comb(w + h - b - 2 - j, w - b - 1) % mod
    ans += tmp
    ans = ans % mod
#    ans = ans + fact[b-1+j]*fact[w+h-b-2-j]/fact[b-1]/fact[j]/fact[w-b-1]/fact[h-1-j]
print((int(ans)))

'''
単純なh*wのマス目だった場合
#h-row / w-col
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
#リスト内包表記で作らないとバグる
#ダメな例 -> con = [[0]*w]*h
#https://qiita.com/utgwkk/items/5ad2527f19150ae33322
print('initialize finished')


for i in range(h-a):
    con[i][0] = 1
#print(con[0])
for j in range(w):
    #wは先に初期化やっちゃう
    con[0][j] = 1
#print(con)

for k in range(1,h-a):
#    print(k)
    for l in range(1,b+1):
        con[k][l] = con[k-1][l] + con[k][l-1]
#print(con[h-a-1][b-1])
#print(con[h-a][b-1])
#print(con[h-a-1][b])

for m in range(1,h):
#    print('---{} row---'.format(m))
#    print(con[m])
    for n in range(b,w):
#        print('m,n:('+str(m)+','+str(n)+')')
        con[m][n] = con[m-1][n] + con[m][n-1]
#    print(con[m])

print(con[h-1][w-1])
'''
