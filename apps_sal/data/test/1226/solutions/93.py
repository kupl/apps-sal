n, a, b = map(int, input().split())

mod = 10**9 + 7

def nck(k):
    y, z = 1, 1
    for i in range(1, k+1):
        y = (y * (n+1-i)) % mod
        z = (z * pow(i, mod-2, mod)) % mod
    return (y*z) % mod

ans = (pow(2, n, mod) - 1 - nck(a) - nck(b)) % mod
print(ans)
