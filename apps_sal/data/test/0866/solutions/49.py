# (i,j)→（i+1,j+2）をx回、(i,j)→（i+2,j+1）がy回あるとすると
# x=(2Y-X)//3,y=(2X-Y)//3、となる
# これが整数or非負なら(x+y)Cxを求めればいい

import sys
X, Y = list(map(int, input().split()))
if (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
    print((0))
    return
if (2 * Y - X) < 0 or (2 * X - Y) < 0:
    print((0))
    return


# それ以外なら存在する
x = (2 * Y - X) // 3
y = (2 * X - Y) // 3
# (x+y)Cxを求める

fac = [0 for i in range(x + y + 1)]
inv = [0 for i in range(x + y + 1)]
finv = [0 for i in range(x + y + 1)]
# 初期条件
fac[0] = fac[1] = 1
inv[1] = 1
finv[0] = finv[1] = 1
p = 1000000007
for i in range(2, x + y + 1):
    fac[i] = (fac[i - 1] * i) % p
    # p=(p//a)*a+(p%a) pの世界で　a^(-1)=-(p//a)*inv[p%a]
    inv[i] = (-(p // i) * inv[p % i]) % p
    finv[i] = (finv[i - 1] * inv[i]) % p

print(((fac[x + y] * finv[x] % p) * finv[y] % p))
