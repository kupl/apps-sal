def add(a, b):
    return (a + b) % mod


def mult(a, b):
    tmp = a % mod * (b % mod)
    return tmp % mod


n = int(input())
c = [int(i) for i in input().split()]
c.sort(reverse=True)
pref = [0] * (n + 1)
pref[0] = 0
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + c[i - 1]
mod = 998244353
invn = pow(n, mod - 2, mod)
for k in range(1, n + 1):
    ans = 0
    j = 0
    for i in range(0, n + 1, k):
        ans = add(ans, mult(j, add(pref[min(n, i + k)], -pref[i])))
        j += 1
    ans = mult(ans, invn)
    print(ans, end=' ')
