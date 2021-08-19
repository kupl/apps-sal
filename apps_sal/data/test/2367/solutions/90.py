import math
(h, w, a, b) = list(map(int, input().split()))
mod = pow(10, 9) + 7


def divmod(num, mod=10 ** 9 + 7):
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
print(int(ans))
'\n単純なh*wのマス目だった場合\n#h-row / w-col\ncon = [[0]*w]*h\nfor i in range(h):\n    con[i][0] = 1\nfor j in range(w):\n    con[0][j] = 1\n\nfor k in range(1,h):\n    for l in range(1,w):\n        con[k][l] = con[k-1][l] + con[k][l-1]\n\nprint(con[h-1][w-1])\n'
"\n全量を計算するやり方\nH*Wがデカすぎると時間というよりもメモリエラー\nprint('initialize')\ncon = [[0 for i in range(w)] for j in range(h)]\n#リスト内包表記で作らないとバグる\n#ダメな例 -> con = [[0]*w]*h\n#https://qiita.com/utgwkk/items/5ad2527f19150ae33322\nprint('initialize finished')\n\n\nfor i in range(h-a):\n    con[i][0] = 1\n#print(con[0])\nfor j in range(w):\n    #wは先に初期化やっちゃう\n    con[0][j] = 1\n#print(con)\n\nfor k in range(1,h-a):\n#    print(k)\n    for l in range(1,b+1):\n        con[k][l] = con[k-1][l] + con[k][l-1]\n#print(con[h-a-1][b-1])\n#print(con[h-a][b-1])\n#print(con[h-a-1][b])\n\nfor m in range(1,h):\n#    print('---{} row---'.format(m))\n#    print(con[m])\n    for n in range(b,w):\n#        print('m,n:('+str(m)+','+str(n)+')')\n        con[m][n] = con[m-1][n] + con[m][n-1]\n#    print(con[m])\n\nprint(con[h-1][w-1])\n"
