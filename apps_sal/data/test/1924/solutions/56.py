
# mod,nについての制約は自分でいかに記入する
mod = 10**9 + 7


def find_power(n, mod):
    # 0!からn!までのびっくりを出してくれる関数(ただし、modで割った値に対してである）
    powlist = [0] * (n + 1)
    powlist[0] = 1
    powlist[1] = 1
    for i in range(2, n + 1):
        powlist[i] = powlist[i - 1] * i % (mod)
    return powlist
 # あるかずxのn乗をmodで割ったあまりを返す関数pow_cal(x,n,mod)


def pow_cal(x, n, mod):
    if n == 0:
        return 1
    elif n == 1:
        return x % mod
    elif n >= 2:
        if n % 2 == 0:
            return (pow_cal(x, n // 2, mod)**2) % mod
        else:
            return (x * pow_cal(x, n // 2, mod)**2) % mod


def find_inv_power(n, mod):
    # 0!からn!までの逆元を素数modで割ったあまりリストを作る関数
    c = 1
    uselist = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        c *= i
        c %= mod
    first = pow_cal(c, mod - 2, mod)
    uselist[n] = first
    for i in range(n, 0, -1):
        uselist[i - 1] = (uselist[i] * i) % (mod)
    return uselist


A = find_power(2 * 10**6 + 10, mod)
B = find_inv_power(2 * 10**6 + 10, mod)


def combi(n, r, mod):
    if n < r:
        return 0
    elif n >= r:
        return (A[n] * B[r] * B[n - r]) % (mod)


r1, c1, r2, c2 = list(map(int, input().split()))

mod = 10**9 + 7

K = combi(r2 + c2 + 2, c2 + 1, mod) - combi(r2 + c1 + 1, c1, mod) - combi(r1 + c2 + 1, r1, mod) + combi(r1 + c1, c1, mod)

print((K % mod))
