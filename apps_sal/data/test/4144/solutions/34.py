n = int(input())
#x, k, d = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]

mod = 10**9 + 7


def modpow(a, n, mod):
    # a^nをmodでわったあまり 二分累乗法O(logn)
    res = 1
    while n > 0:
        if n & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        n = n >> 1
    return res


ans = (modpow(10, n, mod) - modpow(9, n, mod) -
       modpow(9, n, mod) + modpow(8, n, mod)) % mod
print(ans)
