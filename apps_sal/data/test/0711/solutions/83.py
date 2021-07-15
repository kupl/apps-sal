N, M = list(map(int, input().split()))


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])

    if arr == [] and n != 1:
        arr.append([n, 1])

    return arr


mod = 10**9 + 7


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod//i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


primes = factorization(M)
# 何箇所に分けるか（cnt以下）,その中でどう分けるか（しきりをどこにおくか（振り分けられないものが出ると選べれないのとおなじになるので、cnt - 選んだ数））
if N == 1:
    print((1))
    return
ans = 1

for p, cnt in primes:
    tmp = 0
    for i in range(1, min(cnt, N)+1):
        tmp += cmb(N, i, mod) * cmb(cnt-1, i-1, mod)
        #print(tmp, p, cnt, i)
        tmp %= mod
    ans *= tmp
    ans %= mod

print(ans)

