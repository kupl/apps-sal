mod = 998244353
maxn = 1005
'\ndef q_mod(a,b):\n    ans = 1\n    a %= mod\n    while b != 0:\n        if b&1 == 1:\n            ans = ans * a % mod\n            b -= 1\n        b >>= 1\n        a = a * a % mod\n    return ans\n\ndef C(n,m):\n    if m >n :\n        return 0\n    ans = 1\n    for i in range(1,m+1):\n        a = (n + i - m) % mod\n        b = i % mod\n        ans = ans * (a * q_mod(b , mod-2) % mod ) % mod\n    return ans \n\ndef Lucas(n,m):\n    if m == 0:\n        return 1\n    return  C(n % mod,m % mod) * Lucas(int(n/mod) , int(m/mod)) % mod\n'
'\nC = [ ([0]*maxn) for i in range(maxn)]\n\nfor i in range(2,maxn):\n    for j in range(i+1):\n        if j == 0 or j == i:\n            C[i][j] = 1\n            continue;\n        C[i][j] = (C[i-1][j] + C[i-1][j-1]) % mod\n\n\ndef A(n,m):\n    j = 0\n    ans = 1\n    for i in range(0,n+1):\n        if j == m:\n            break\n        j += 1\n        ans = (ans * (n - i)) % mod\n    return ans\n\n'


def solve(n, m):
    if n > m:
        (n, m) = (m, n)
    (ans, s) = (0, 1)
    for i in range(0, n + 1):
        ans = ans + s
        s = s * (n - i) // (i + 1) * (m - i)
    return ans


while True:
    try:
        (a, b, c) = list(map(int, input().split()))
        print(solve(a, b) * solve(a, c) * solve(b, c) % mod)
    except:
        break
