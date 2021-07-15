def readinput():
    n,k=list(map(int,input().split()))
    return n,k

# 法Pの下での組み合わせ数 nCk を求める
# MAX: nの最大値

MAX = 2000+5  # (X+Y)/3より大きい整数 1 <= X, Y <= 10**6
MOD = (10**9)+7

fac=[1 for x in range(MAX)]
inv=[1 for x in range(MAX)]
finv=[1 for x in range(MAX)]

# 拡張ユークリッドアルゴリズム
# (d, x, y): d=ax+by を満たすd, x, yを求める
# aとbが互いに素な整数であればgcd(a,b)=d=1, ax=1 (mod b)
# xは法bの元でaの乗法逆元a^-1になる
def exEuclid(a, b):
    if (b==0):
        return (a, 1, 0)
    else:
        (dd, xx, yy) = exEuclid(b, a % b)
        return (dd, yy, xx - (a//b)*yy)

def COMinit():
    for i in range(2,MAX):
        #print(i,fac)
        fac[i] = fac[i-1]*i % MOD
        (d, x, y) = exEuclid(i, MOD)
        inv[i] = x
        finv[i] = finv[i-1]*inv[i] % MOD

def COM(n, k):
    if(n<k):
        return 0
    elif ( (n<0)or(k<0)):
        return 0
    else:
        return fac[n]*(finv[n-k]*finv[k] % MOD) % MOD




def main(n,k):
    COMinit()
    m=n-k+1
    for i in range(1,k+1):
        if i > min(m,k):
            print((0))
        else:
            print(( ( COM(m,i)*COM(k-1,i-1) ) %MOD ))

def __starting_point():
    n,k=readinput()
    main(n,k)

__starting_point()
