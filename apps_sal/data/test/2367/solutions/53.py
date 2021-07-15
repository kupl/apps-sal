# 練習
import math
h,w,a,b = list(map(int, input().split()))
p = 10**9+7
# 方針
# (0,0)    ~ (0,w-1)
# (h-1,0 )~ (h-1,w-1)で考える
# 通れないのは(h-a) ~ (h-1)行かつ(0) ~ (b-1) 列のところ
# b <= i <= w-1 のiについて1,2,3の組み合わせはそれぞれ以下の通り 
# 1, (0,0) ~ (h-a-1,i)      (h-a-1+i)! /(h-a-1)! * i!
# 2, (h-a-1,i )~(h-a,i)　  1
# 3, (h-a,i) ~ (h-1,w-1)   (a-1+w-1-i)! /(a-1)! * (w-1-i)!
def cmb(n, k, mod, fac, ifac):
    """
    nCkを計算する
    """
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod


def make_tables(mod, n):
    """
    階乗テーブル、逆元の階乗テーブルを作成する
    """
    fac = [1, 1] # 階乗テーブル・・・(1)
    ifac = [1, 1] #逆元の階乗テーブル・・・(2)
    inverse = [0, 1] #逆元テーブル・・・(3)

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac

fac, ifac = make_tables(p, h+w-2)
total = 0
for i in range(b, w):
    r1 = cmb(h-a-1+i,i,p,fac, ifac)
    r3 = cmb(a-1+w-1-i, a-1,p,fac, ifac)
    
    total = total +( r1*r3)
print(total%p)   
